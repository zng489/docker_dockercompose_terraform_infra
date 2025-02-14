"""
import pika

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue='hello')

# Set up the consumer to listen to the queue
channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
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

    # Declare a durable queue to make sure it exists
    channel.queue_declare(queue='task_queue', durable=True)

    # Set the prefetch count to limit the number of unacknowledged messages
    channel.basic_qos(prefetch_count=1)  # Consumer only gets 1 unacknowledged message at a time

    return connection, channel

def process_message(ch, method, properties, body):
    # Simulate some work by sleeping
    print(f"Received: {body.decode()}")
    time.sleep(random.randint(1, 5))  # Simulate a time-consuming task
    print(f"Processed: {body.decode()}")
    
    # Acknowledge the message after processing
    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    connection, channel = create_channel()

    # Set up the consumer
    channel.basic_consume(
        queue='task_queue', 
        on_message_callback=process_message
    )

    print('Waiting for messages. To exit press CTRL+C')
    try:
        # Start consuming
        channel.start_consuming()
    except KeyboardInterrupt:
        print("Consumer interrupted.")
    finally:
        # Close the connection gracefully
        connection.close()

if __name__ == "__main__":
    main()
"""


import pika
import json
from opensearchpy import OpenSearch

# Configuração simplificada do cliente OpenSearch
host = 'localhost'
port = 9200
auth = ('admin', 'J!x2Vb9z*') # For testing only. Don't store credentials in code.
ca_certs_path = '/full/path/to/root-ca.pem' # Provide a CA bundle if you use intermediate CAs with your root CA.

# Create the client with SSL/TLS enabled, but hostname verification disabled.
client = OpenSearch(
    hosts = [{'host': host, 'port': port}],
    http_compress = True, # enables gzip compression for request bodies
    http_auth = auth,
    use_ssl = True,
    verify_certs = False,
    ssl_assert_hostname = False,
    ssl_show_warn = False,
    ca_certs = ca_certs_path
)

# Nome do índice no OpenSearch
index_name = "my_index"

# Função para verificar se o dado existe no OpenSearch
def check_data_exists(data_id):
    try:
        response = client.get(index=index_name, id=data_id)
        return True  # O dado existe
    except Exception as e:
        return False  # O dado não existe

# Função para inserir dados no OpenSearch
def ingest_to_opensearch(data):
    response = client.index(index=index_name, body=data)
    print(f"Data ingested into OpenSearch: {response['result']}")

# Função que será chamada quando a mensagem for recebida do RabbitMQ
def callback(ch, method, properties, body):
    message = json.loads(body)
    print(f"Received message: {message}")
    
    # Verificar se o dado já existe no OpenSearch
    if not check_data_exists(message['id']):
        ingest_to_opensearch(message)  # Inserir no OpenSearch se não existir
    else:
        print("Data already exists in OpenSearch.")

# Configuração do RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='my_queue')

# Consumir as mensagens da fila
channel.basic_consume(queue='my_queue', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()