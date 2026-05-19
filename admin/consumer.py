

import pika, json

from admin.products.models import Product

params = pika.ConnectionParameters('amqps://nhzsened:sghwS0lh1e9inlPPL40Zs2AU53RAVzCJ@capybara.lmq.cloudamqp.com/nhzsened   ')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin', durable=True)

def callback(ch, method, properties, body):
    id = json.loads(body)
    print(body)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('increased')

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('start')

channel.start_consuming()

channel.close()