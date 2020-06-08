#!/usr/bin/env python
import pika
from os import environ
from time import sleep

try:
	connection = pika.BlockingConnection(pika.ConnectionParameters(host=environ.get('RABBITMQ_HOST', 'rabbit')))
except pika.exceptions.AMQPConnectionError as e:
	print('Error: Connecting to RabbitMQ')
	exit(1)

channel = connection.channel()

channel.queue_declare(queue='hello')

try:
	while True:
		channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
		print(" [x] Sent 'Hello World!'")
		sleep(0.5)
except KeyboardInterrupt as e:
	connection.close()