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

    searched_state = session.query(State).filter(State.name == argv[4]).first()
    if searched_state is None:
        print('Not found')
    else:
        print(searched_state.id)

    session.close()


if __name__ == '__main__':
    """
        the main function
    """
    run_database()
