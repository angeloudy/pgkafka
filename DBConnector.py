import psycopg2
import logging

logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', filename='./db.log')
class DBConnector:
    def __init__(self, host='localhost', db='postgres', user='user', password='pass'):
        try:
            self.conn = psycopg2.connect(host=host, database=db, user=user, password=password)
        except Exception as e:
            self.conn = None

    # create table from json
    def create_table(self, tbl_name, schema):
        #id = {'id': 'SERIAL'}  # add id column
        #schema = {**id, **schema}
        columns = [f'{column} {datatype}' for column, datatype in schema.items()]
        query = ', '.join(columns)
        query = f'CREATE TABLE IF NOT EXISTS {tbl_name} ({query});'
        try:
            logging.debug(f'creating table, sql: {query}')
            self.run_query(query)
        except Exception as e:
            logging.error(f'error while creating table {tbl_name}, {e}')
            return False

    # run a sql query and return result
    def run_query(self, query):
        cur = self.conn.cursor()
        try:
            cur.execute(query)
            self.conn.commit()
        except Exception as e:
            logging.error(f'Error while executing query {query}', {e})


connector = DBConnector('localhost', db='taozhou', user='taozhou', password='')
table = {
    'name': "varchar(20)",
    'value': 'varchar(20)',
    'clock': 'int'
}

connector.create_table('osmetrics', table)



