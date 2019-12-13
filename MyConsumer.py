from kafka import KafkaConsumer
import json
from DBConnector import DBConnector

class MyConsumer:
    def __init__(self):
        pass

    def run(self):
        config = json.load(open('config/psql.json'))
        connector = DBConnector(**config)
        table = {
            'name': "varchar(20)",
            'value': 'varchar(20)',
            'clock': 'int'
        }

        METRIC_TABLE = 'osmetrics'
        connector.create_table(METRIC_TABLE, table)

        KAFKA_SERVER = "127.0.0.1:9092"

        consumer = KafkaConsumer('osmetrics', bootstrap_servers=KAFKA_SERVER)
        for msg in consumer:
            data = json.loads(msg.value.decode('utf-8'))
            query = f'INSERT INTO {METRIC_TABLE} values {str(tuple(data.values()))}'
            connector.run_query(query)

myconsumer = MyConsumer()
myconsumer.run()