import psutil
import json
from kafka.producer import KafkaProducer
import time

KAFKA_SERVER = "127.0.0.1:9092"


def collect_metrics():
    metrics = {
        'name': 'cpu_usage',
        'value': int(psutil.cpu_percent()),
        'clock': int(time.time())
    }
    return metrics


producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
while True:
    f = producer.send('first_topic', json.dumps(collect_metrics()).encode('utf-8'))
    producer.flush()
    time.sleep(5)



