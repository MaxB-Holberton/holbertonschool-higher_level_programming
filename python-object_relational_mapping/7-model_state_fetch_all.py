#!/usr/bin/python3
"""
    Module for connecting to MySQL and grabbing states
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def run_database():
    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(url)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

    session.close()


if __name__ == '__main__':
    """
        the main function
    """
    run_database()
