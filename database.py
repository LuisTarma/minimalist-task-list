from sqlite3 import connect, Error, version
import db_map

QUERIES = db_map.db_map()

def create_connection(db_file):
    conn = None 
    try:
        conn = connect(db_file)
        print("Sqlite version: " + version)
    except Error as e:
        print(e)
    return conn

def create_table(connection):
    try:
        c = connection.cursor()
        c.execute(QUERIES.createTableNotes_sql())
    except Error as e:
        print(e)

def insertNote(connection, note):
    cur = connection.cursor()
    cur.execute(QUERIES.insertNote_sql(), note)
    return cur.lastrowid

def updateNote(connection, note):
    cur = connection.cursor()
    cur.execute(QUERIES.updateNote_sql(), note)
    connection.commit()

def main():
    """
    Test 
    """
    connection = create_connection("notes.db")
    ######## Create table notes if not exist ############################################
    if connection is not None:
        create_table(connection, QUERIES.createTableNotes_sql())
    else:
        print("Cannot create database connection")
    #####################################################################################
    note = (1, "test note")
    insertNote(connection, note)
    unote = ("test update", 1)
    updateNote(connection, unote) 
    connection.close()
