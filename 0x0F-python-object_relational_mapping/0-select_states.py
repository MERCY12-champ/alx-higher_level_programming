#!/usr/bin/python3
"""
Script that list all states from the database hbtn_0e_0_usa:
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("select * FROM states")
    [print(state) for state in cur.fetchAll()]
