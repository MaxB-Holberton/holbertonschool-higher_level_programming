#!/usr/bin/python3
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


"""
    Module for connecting to MySQL and grabbing states
"""


def run_database():
    engine = create_engine('mysql+mysqldb://{}:\
        {}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))

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
