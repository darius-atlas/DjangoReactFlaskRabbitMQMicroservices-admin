
import pika

params = pika.URLParameters('amqps://ivftybvf:rcz0oRvPEQfs8zPDEAcc1zzzwDIQtcze@beaver.rmq.cloudamqp.com/ivftybvf')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Callback to admin')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback)

print('Startd Consuming')

channel.start_consuming()

channel.close()

