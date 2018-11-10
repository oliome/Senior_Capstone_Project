#!/usr/bin/python
 
import sqlite3
import sys
from sqlite3 import Error
 
 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def profile_table_setup(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS profiles (name STRING NOT NULL,user_db STRING NOT NULL);")

def create_profile(conn,name):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("INSERT INTO profiles (name,user_db) values (\""+str(name)+"\",\""+str(name.lower())+"_db\");")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS "+str(name.lower())+"_db(barcode INTEGER NOT NULL,item_name STRING NOT NULL, exp DATE);")
def delete_profile(conn,name):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("DELETE FROM profiles WHERE name =\""+name+"\";")
    cur.execute("DROP "+ str(name.lower())+"_db;")


 
def select_all_profiles(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM profiles;")
 
    rows = cur.fetchall()
    
    for row in rows:
        print(row[0]+", "+row[1])
 
 
def select_profile_db(conn, name):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param name: name of profile wanted
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT name FROM profiles WHERE name=\""+name+"\";")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row[0])


 
 
def main():
    database = "gro_log.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        profile_table_setup(conn)
        add = raw_input("Name you would like to add:")
        #delete= input("Name you would like to delete:")
        name= raw_input("Name you would like to select:")
        create_profile(conn,add)
        #delete_profile(conn,delete)
        #print("\n1. Query profiles by name:")
        select_profile_db(conn,name)
 
        print("\n2. Query all profiles")
        select_all_profiles(conn)
 
 
if __name__ == '__main__':
    main()
