import pika 
import json
import os 
def publish_message(exchange_name, body):
    try:
       params = pika.URLParameters(os.getenv('CELERY_BROKER_URL'))
       connection = pika.BlockingConnection(params)
       channel = connection.channel()
       channel.exchange_declare(exchange=exchange_name,exchange_type='fanout')
       channel.basic_publish(
           exchange=exchange_name,routing_key='',body=json.dumps(body,default=str),
           properties=pika.BasicProperties(content_type='application/json',delivery_mode=2)
       )
       print(f" [x] Sent event to '{exchange_name}': {body}")
       connection.close()     

    except Exception as e:
        print(f"ERROR: Could not publish event to '{exchange_name}'. Error: {e}")

