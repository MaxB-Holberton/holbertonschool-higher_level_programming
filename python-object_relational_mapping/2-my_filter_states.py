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
    db_cursor.execute("SELECT * FROM states WHERE name \
        LIKE BINARY '{}' ORDER BY states.id ASC".format(argv[4]))

    for state in db_cursor.fetchall():
        print(state)

    if db_cursor:
        db_cursor.close()
    if db:
        db.close()


if __name___ = '__main__':
    """
        the main function
    """
    run_database()
