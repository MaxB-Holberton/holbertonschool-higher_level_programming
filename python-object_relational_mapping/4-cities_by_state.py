#!/usr/bin/python3
from sys import argv
import MySQLdb


"""
    Module for connecting to MySQL and grabbing states
"""


def run_database():
    """
        Function to connect to the database and perform the sort
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], database=argv[3])

    db_cursor = db.cursor()
    db_cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
        JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")

    for city in db_cursor.fetchall():
        print(city)

    if db_cursor:
        db_cursor.close()
    if db:
        db.close()


if __name___ = '__main__':
    run_database()
