from pgkafka.Consumer.MyConsumer import MyConsumer
from pgkafka.Producer.MyProducer import MyProducer
from multiprocessing import Process

def run_consumer():
    consumer = MyConsumer()
    consumer.startd()

def run_producer():
    producer = MyProducer()
    producer.startd()


def main():
    print('HHHHHH')

    p1 = Process(target=run_consumer)
    p1.start()
    p2 = Process(target=run_producer)
    p2.start()

if __name__ == '__main__':
    main()