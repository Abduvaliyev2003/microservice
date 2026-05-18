import pika

params = pika.ConnectionParameters('amqps://nhzsened:sghwS0lh1e9inlPPL40Zs2AU53RAVzCJ@capybara.lmq.cloudamqp.com/nhzsened   ')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='nhzsened',routing_key='main', body='Hello World')

