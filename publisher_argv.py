import pika, sys
import json
import time
from random import randint
import sys

            
credentials = pika.PlainCredentials('guest', 'guest')

conn_params = pika.ConnectionParameters("localhost", credentials = credentials)

conn_broker = pika.BlockingConnection(conn_params)

channel = conn_broker.channel()
channel.queue_declare(queue = "response-queue")
channel.queue_bind(queue = "response-queue",
                   exchange = "response-exchange",
                   routing_key = "response")
channel.exchange_declare(exchange='response-exchange',
                         exchange_type = "direct",
                         passive = False,
                         durable = True,
                         auto_delete = False)

#msg = sys.argv[1]
msg_props = pika.BasicProperties()
msg_props.content_type = "application/json"
number = 0


 
    
string_json = {"path_cut_tif": sys.argv[1], "id_request":sys.argv[2]}
channel.basic_publish(body=json.dumps(string_json),
                      exchange = "response-exchange",
                      properties = msg_props,
                      routing_key="response")   
