import duckdb
import os
import pathlib

db_file = '../datalake.db'

for file in os.listdir('sources') :

    csv_file = f'sources/{file}'

    table_name = pathlib.Path(file).stem

    with duckdb.connect(db_file) as conn :

        try:
            conn.execute(f"""CREATE TABLE {table_name} AS SELECT * FROM read_csv_auto('{csv_file}')""")
            
            result = conn.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()
            print("\033[32m" + f"Nombre de lignes insérées dans {table_name}: {result[0]}" + "\033[0m")

        except Exception as e:
            print("\033[31m" + f"Une erreur s'est produite : {e}" + "\033[0m")

        # conn.sql(f"""SELECT * FROM {table_name} LIMIT 5""").show()