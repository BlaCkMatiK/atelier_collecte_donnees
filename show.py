import duckdb
import os
import pathlib

db_file = 'datalake.db'

table = input('Quelle table ? ')
limit = int(input('Quelle limite ? '))

with duckdb.connect(db_file) as conn :
    conn.sql(f"""SELECT * FROM {table} LIMIT {limit}""").show()