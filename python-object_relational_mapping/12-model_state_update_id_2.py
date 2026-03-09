#!/usr/bin/python3
"""
    Module for connecting to MySQL and grabbing states
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def run_database():
    """
        Function to connect to the database and perform the sort
    """
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])
    engine = create_engine(url)

    Session = sessionmaker(bind=engine)
    session = Session()

    searched_state = session.query(State).filter(State.id == 2)
    searched_state.name = 'New Mexico'
    session.commit()

    session.close()


if __name__ == '__main__':
    """
        the main function
    """
    run_database()
