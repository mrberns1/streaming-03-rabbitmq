"""
    This program sends a message to a queue on the RabbitMQ server.

    Author: Denise Case
    Date: January 14, 2023
    Edit: Missy Bernskoetter, 1/30/2023

"""

# add imports at the beginning of the file
import pika
import sys
import os

def send_message(host: str('localhost'), queue_name: str('Missy'), message: str('favorite author')):
    """
    Creates and sends a message to the queue each execution.
    This process runs and finishes.

    Parameters:
        queue_name (str): the name of the queue
        message (str): the message to be sent to the queue

    """

    try:
        # create a blocking connection to the RabbitMQ server
        conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
        # use the connection to create a communication channel
        ch = conn.channel()
        # use the channel to declare a queue
        ch.queue_declare(queue='Missy')
        # use the channel to publish a message to the queue
        ch.basic_publish(exchange="", routing_key='Missy', body='Chuck Palahniuk')
        # print a message to the console for the user
        print(f" [x] Sent 'Chuck Palahniuk'")
    except pika.exceptions.AMQPConnectionError as e:
        print(f"Error: Connection to RabbitMQ server failed: {e}")
        sys.exit(1)
    finally:
        # close the connection to the server
        conn.close()

# Standard Python idiom to indicate main program entry point
# This allows us to import this module and use its functions
# without executing the code below.
# If this is the program being run, then execute the code below
if __name__ == "__main__":
    send_message("localhost","Missy","favorite author")