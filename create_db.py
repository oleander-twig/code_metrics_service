from clickhouse_driver import Client


client = Client(host='localhost')

client.execute('CREATE DATABASE IF NOT EXISTS code_metrics_service')

client.execute('CREATE TABLE IF NOT EXISTS repos (repo_name String)')

client.execute('INSERT INTO repos VALUES %(a)s', {'a': "test"})