import pika 


def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,))

def get_task():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # does nothing if the queue exists 
    channel.queue_declare(queue='tasks') 

    channel.basic_consume(callback, queue='tasks', no_ack=True)

    # waits for messages 
    channel.start_consuming()