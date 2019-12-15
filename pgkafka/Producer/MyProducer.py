import psutil
import json
from kafka.producer import KafkaProducer
import time
from pgkafka.defs import ROOT_DIR

class MyProducer:
    def __init__(self):
        pass

    def collect_metrics(self):
        metrics = {
            'name': 'cpu_usage',
            'value': int(psutil.cpu_percent()),
            'clock': int(time.time())
        }
        return metrics

    def startd(self):
        collect_interval = 5
        with open(f'{ROOT_DIR}/config/kafka.json') as conf:
            kafka_config = json.load(conf)
        producer = KafkaProducer(**kafka_config)
        while True:
            f = producer.send('osmetrics', json.dumps(self.collect_metrics()).encode('utf-8'))
            producer.flush()
            time.sleep(collect_interval)

