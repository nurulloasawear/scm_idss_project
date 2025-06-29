import pika
import time
import os
import json
import django
import traceback
from django.core.management.base import BaseCommand
from django.db import close_old_connections
# YECHIM: Sozlamalarni to'g'ridan-to'g'ri Django'dan import qilish
from django.conf import settings

# Django muhitini sozlash
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "logistics_service.settings")
django.setup()

from logistics.models import Shipment

class Command(BaseCommand):
    help = 'Starts the RabbitMQ consumer for logistics service'

    def process_logistics_event(self, ch, method, properties, body):
        try:
            close_old_connections()
            data = json.loads(body)
            event_type = data.get('event_type')
            self.stdout.write(self.style.SUCCESS(f" [x] Received event: {event_type}"))

            if event_type == 'ORDER_CREATED':
                order_id = data.get('id')
                if not order_id:
                    self.stderr.write(self.style.ERROR(" [!] ERROR: 'id' not found in order data."))
                elif Shipment.objects.filter(customer_order_id=order_id).exists():
                    self.stdout.write(self.style.SUCCESS(f" [i] INFO: Shipment for order {order_id} already exists. Skipping."))
                else:
                    Shipment.objects.create(customer_order_id=order_id)
                    self.stdout.write(self.style.SUCCESS(f" [+] SUCCESS: Created new shipment for order {order_id}."))
            
            ch.basic_ack(delivery_tag=method.delivery_tag)

        except Exception as e:
            self.stderr.write(self.style.ERROR(f" [!] ERROR in callback: {e}"))
            self.stderr.write(traceback.format_exc())
            ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

    def handle(self, *args, **options):
        # YECHIM: broker_url endi Django sozlamalaridan olinmoqda
        broker_url = settings.CELERY_BROKER_URL
        if not broker_url:
            self.stderr.write(self.style.ERROR("CELERY_BROKER_URL not found in Django settings."))
            return

        while True:
            try:
                self.stdout.write('Connecting to RabbitMQ for logistics...')
                params = pika.URLParameters(broker_url)
                connection = pika.BlockingConnection(params)
                channel = connection.channel()

                channel.exchange_declare(exchange='orders_exchange', exchange_type='fanout')
                result = channel.queue_declare(queue='', exclusive=True)
                queue_name = result.method.queue
                channel.queue_bind(exchange='orders_exchange', queue=queue_name)

                self.stdout.write(self.style.SUCCESS(' [*] Waiting for order events. To exit press CTRL+C'))
                
                channel.basic_consume(
                    queue=queue_name, 
                    on_message_callback=self.process_logistics_event,
                    auto_ack=False
                )
                
                channel.start_consuming()

            except pika.exceptions.AMQPConnectionError as e:
                self.stderr.write(self.style.ERROR(f"Connection to RabbitMQ failed: {e}. Retrying..."))
                time.sleep(5)
            except KeyboardInterrupt:
                self.stdout.write(self.style.SUCCESS('Consumer stopped.'))
                break
            except Exception as e:
                self.stderr.write(self.style.ERROR(f"An unexpected error occurred in main loop: {e}"))
                self.stderr.write(traceback.format_exc())
                time.sleep(10)
