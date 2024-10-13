import duckdb
import os
import pathlib

db_file = 'datalake.db'

with duckdb.connect(db_file) as conn :
    conn.sql(f"""SHOW TABLES""").show()

    table = input('Quelle table ? ')
    limit = int(input('Quelle limite ? '))

    conn.sql(f"""SELECT * FROM {table} LIMIT {limit}""").show()
    conn.sql(f"""DESCRIBE {table}""").show()