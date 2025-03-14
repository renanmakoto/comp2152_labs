import sqlite3
from contextlib import closing
db_path = "test.db"
try:
    with (sqlite3.connect(db_path)) as db_connection:
        db_connection.row_factory = sqlite3.Row
        with closing(db_connection.cursor()) as cursor:
            try:
                query_1 = "SELECT * FROM demo WHERE id > 14"
                cursor.execute(query_1)
                rows = cursor.fetchall()
                print("Name of rows with id > 14")
                for row in rows:
                    print(row["name"])
            except Exception as e:
                print(f"Error executing query_1: {e}")
            #To delete one or more rows based on user input
            try:
                del_row = int(input("Enter the row ID threshold for deletion: "))
                query_2 = "DELETE FROM demo WHERE id < ?"
                cursor.execute(query_2, (del_row, ))
                num_rows = cursor.rowcount
                print(f"{num_rows} a affected.")
                db_connection.commit()
            except Exception as e:
                print(f"Error executing query 1: {e}")
except sqlite3.Error as e:
    print(f"Database connection Error: {e}")
