
import pika

params = pika.URLParameters('amqps://ivftybvf:rcz0oRvPEQfs8zPDEAcc1zzzwDIQtcze@beaver.rmq.cloudamqp.com/ivftybvf')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='admin', body='hello')
