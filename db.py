#!/usr/bin/python
import MySQLdb

def get_user(user, password):
    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                         user="root",         # your username
                         passwd="cookies",  # your password
                         db="hacknc")        # name of the data base

    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()

    # Use all the SQL you like
    cur.execute("SELECT NesID FROM auth")

    # print all the first cell of all the rows
    rtn = ""
    for row in cur.fetchall():
        rtn = row[0]

    db.close()
    print(rtn)
    return rtn

if __name__ == "__main__":
    get_user("", "")
