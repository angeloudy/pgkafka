from kafka import KafkaConsumer
import json
from pgkafka.db.DBConnector import DBConnector
from pgkafka.defs import ROOT_DIR

class MyConsumer:
    def __init__(self):
        pass

    def startd(self):
        config = json.load(open(f'{ROOT_DIR}/config/psql.json'))
        connector = DBConnector(**config)
        table = {
            'name': "varchar(20)",
            'value': 'varchar(20)',
            'clock': 'int'
        }

        METRIC_TABLE = 'osmetrics'
        connector.create_table(METRIC_TABLE, table)

        with open(f'{ROOT_DIR}/config/kafka.json') as conf:
            kafka_config = json.load(conf)
        consumer = KafkaConsumer('osmetrics', **kafka_config)
        for msg in consumer:
            data = json.loads(msg.value.decode('utf-8'))
            query = f'INSERT INTO {METRIC_TABLE} values {str(tuple(data.values()))}'
            connector.run_query(query)

