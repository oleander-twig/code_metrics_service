import pika 


def create_task(task):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # does nothing if the queue exists 
    channel.queue_declare(queue='tasks') 

    channel.basic_publish(exchange='', routing_key='tasks', body=task)

    connection.close()