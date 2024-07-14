import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

connection = sqlite3.connect(ROOT_PATH / "database.sqlite")

# in order to run commands in the database, creating a cursor is required

cursor = connection.cursor()

# and to actually execute a command, a commit is required

# creating table
def create_table(connection, cursor):
    cursor.execute(
        "CREATE TABLE clients (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255), email VARCHAR(255))"
    )
    connection.commit()

# inserting row
def insert_into(connection, cursor, name, email):
    data = (name, email) # tuple
    cursor.execute("INSERT INTO clients (name, email) VALUES (?,?);", data)
    connection.commit()

# insert multiple rows
def insert_many(connection, cursor, data):
    cursor.executemany("INSERT INTO clients (name, email) VALUES (?,?)", data)
    connection.commit()

# updating row
def update(connection, cursor, name, email, id):
    data = (name, email, id)
    cursor.execute("UPDATE clients SET name=?, email=? WHERE id=?;", data)
    connection.commit()

# deleting row
def delete(connection, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clients WHERE id=?;", data)
    connection.commit()

# fetch single row
def fetchone(cursor, id):
    cursor.execute("SELECT * FROM clients WHERE id=?", (id,))
    return cursor.fetchone()

# fetch multiple rows
def fetchall(cursor): # to access the data, iterate through the returning object
    return cursor.execute("SELECT * FROM clients;")

clients = fetchall(cursor)
for client in clients:
    print(client)

# data = [
#     ("v", "vitor@gmail.com"),
#     ("k", "kenzo@gmail.com"),
#     ("k", "koga@gmail.com"),
#     ("o", "onoue@gmail.com")
# ]




# this is prone to sql injection

# name = "vkko"
# email = "vitork.onoue@gmail.com"
# cursor.execute(f"INSERT INTO clientes (name, email) VALUES ('{name}', '{email}');")

# this is better