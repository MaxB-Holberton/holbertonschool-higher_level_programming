#!/usr/bin/python3
"""
    Module for connecting to MySQL and grabbing states
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def run_database():
    """
        Function to connect to the database and perform the sort
    """
    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(url)

    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()
    if first_state is None:
        print('Nothing')
    else:
        print('{}: {}'.format(first_state.id, first_state.name))

    session.close()


if __name__ == '__main__':
    """
        the main function
    """
    run_database()
