#!/usr/bin/python
 
import sqlite3
import sys
from sqlite3 import Error
 
 
def create_connection():
    """ create a  connection to the SQLite 
        specified by the db_file
    :param db_file:  file
    :return: Connection object or None
    """
    db_file= "gro_log.db"
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def profile_table_setup():
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS profiles (name STRING NOT NULL,user_db STRING NOT NULL)")

def create_profile(name):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT or IGNORE INTO profiles (name,user_db) values (\""+str(name)+"\",\""+str(name.lower())+"_db\")")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS "+str(name.lower())+"_db(barcode INTEGER,item_name STRING NOT NULL, exp DATE)")

def delete_profile(name):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM profiles WHERE name =\""+name+"\"")
        cur=conn.cursor()
        cur.execute("DROP TABLE "+ str(name.lower())+"_db")


 
def select_all_profiles():
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM profiles")
    
        rows = cur.fetchall()
        array=[]
        for row in rows:
            array.append(row[0])
        return array

def count_exp(name):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param name: name of profile wanted
    :return:
    """
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM `"+str(name.lower())+"_db` WHERE exp > date('now', '+7 days');")
    
        rows = cur.fetchall()
        return rows[0][0]

def select_inventory(name):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param name: name of profile wanted
    :return:
    """
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM "+str(name.lower())+"_db")
    
        rows = cur.fetchall()
        array=[]
        max_len=0
        for row in rows:
                if len(row[1]) > max_len:
                        max_len=len(row[1])
        for row in rows:
                temp=str(row[1])
                x=0
                pad=" "
                length= len(temp)
                if length < max_len:
                        temp=(pad*(max_len-length)*2)+" "+temp

                while x <= (58-length):
                        temp= temp+pad
                        x+=1
                temp=temp+str(row[2])+pad*48+str(row[0])
                if length < max_len:
                        temp=temp+(pad*(max_len-length))
                array.append(temp)
        return array

def add_inventory(name,item_info):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param name: name of profile wanted
    :return:
    """
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO "+str(name.lower())+"_db (barcode,item_name,exp) values ("+str(item_info[1])+",\""+str(item_info[0])+"\",\""+str(item_info[2])+"\")")

def delete_inventory(name,item_name):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param name: name of profile wanted
    :return:
    """
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM "+str(name.lower())+" WHERE item_name=\""+item_name+"\"")

def select_profile_db(name):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param name: name of profile wanted
    :return:
    """
    conn = create_connection()
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT name FROM profiles WHERE name=\""+name+"\"")
 
        rows = cur.fetchall()
        array=[]
        for row in rows:
            array.append(row[0])
        print(array)
        return array

 
 
#def main():

        #profile_table_setup()
        #--------Add Profile Test------------
        #add = input("Name you would like to add:")
        #create_profile(add)

        #print(select_all_profiles())

        #-------Delete Profile Test----------
        #delete= input("Name you would like to delete:")
        #delete_profile(conn,delete)

        #-------Select Profile Test----------
        #name= raw_input("Name you would like to select:")
        #select_profile_db(conn,name)
 
        #-------Show All Profiles Test-------
        #print("\n2. Query all profiles")
        #select_all_profiles(conn)

        #-------Add Item Test---------
        #name=input("Database name: ")
        #barcode=input("Barcode: ")
        #item_name=input("Item name: ")
        #exp_date=input("Exp Date(YYYY-MM-DD): ")
        #add_inventory(name,barcode,item_name,exp_date)

        #select_inventory("Zack")
 
 
#if __name__ == '__main__':
#   main()
