import sqlite3

DB_NAME = "sqllite_db.db"

with sqlite3.connect(DB_NAME) as sqllite_conn:
    print(sqllite_conn)
    print(sqlite3.version)

