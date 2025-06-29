import pika 
import json
import os 
from django.db import transaction
from .models import inventory as Inventory
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "inventory_service.settings")
django.setup()

from django.db import transaction


def process_inventory_event(ch, method, properties, body):
    try:
        data = json.loads(body)
        event_type = data.get('event_type')

        print(f" [x] Received event '{event_type}': {data}")

        if event_type == 'DECREASE_STOCK':
            with transaction.atomic():
                order_items = data.get('items', [])
                for item in order_items:
                    product_id = item.get('product_id')
                    quantity_to_decrease = item.get('quantity')

                    if not product_id or not quantity_to_decrease:
                        continue
                    
                    inventory_item = Inventory.objects.select_for_update().filter(product_id=product_id).first()

                    if inventory_item:
                        if inventory_item.quantity >= int(quantity_to_decrease):
                            inventory_item.quantity -= int(quantity_to_decrease)
                            inventory_item.save()
                            print(f" > Stock for product {product_id} decreased by {quantity_to_decrease}. New quantity: {inventory_item.quantity}")
                        else:
                            print(f" ! WARNING: Not enough stock for product {product_id}. Required: {quantity_to_decrease}, Available: {inventory_item.quantity}")
                    else:
                        print(f" ! WARNING: Inventory record not found for product {product_id}.")

        ch.basic_ack(delivery_tag=method.delivery_tag)

    except json.JSONDecodeError:
        print(" [!] ERROR: Could not decode message body.")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
    except Exception as e:
        print(f" [!] ERROR: An unexpected error occurred: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

