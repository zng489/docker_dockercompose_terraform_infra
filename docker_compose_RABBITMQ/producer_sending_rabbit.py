"""
import pika

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue (it will be created if it doesn't exist)
channel.queue_declare(queue='hello')

# Send a message to the queue
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

print(" [x] Sent 'Hello World!'")

# Close the connection
connection.close()
"""



"""
import pika
import time
import random
import sys

# Connection parameters
connection_params = pika.ConnectionParameters('localhost')

def create_channel():
    # Establish a connection and channel
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    # Declare a durable queue (messages will be persisted)
    channel.queue_declare(queue='task_queue', durable=True)

    return connection, channel

def send_message(channel, message):
    # Publish a message to the queue with a persistence flag
    channel.basic_publish(
        exchange='',          # Default exchange
        routing_key='task_queue',  # The queue name
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2,  # Make the message persistent
        )
    )
    print(f"Sent: {message}")

def main():
    connection, channel = create_channel()
    
    try:
        while True:
            # Simulate some random task
            message = f"Task-{random.randint(1, 100)}"
            send_message(channel, message)
            time.sleep(random.randint(1, 3))  # Sleep between sends

    except KeyboardInterrupt:
        print("Producer interrupted.")
    finally:
        # Close the connection gracefully
        connection.close()

if __name__ == "__main__":
    main()
"""

import pika
import json

def send_message_to_rabbitmq(queue_name, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    channel.basic_publish(exchange='',
                          routing_key=queue_name,
                          body=json.dumps(message))
    print(f"Sent message: {message}")
    connection.close()

# Exemplo de dado
message = {
    "id": 1,
    "name": "Item Exemplo",
    "description": "Descrição do item."
}

# Enviar o dado para RabbitMQ
send_message_to_rabbitmq('my_queue', message)