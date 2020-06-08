#!/usr/bin/env python
import pika
from os import environ

try:
	connection = pika.BlockingConnection(pika.ConnectionParameters(host=environ.get('RABBITMQ_HOST', 'rabbit')))
except pika.exceptions.AMQPConnectionError as e:
	print('Error: Connecting to RabbitMQ')
	exit(1)

channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()