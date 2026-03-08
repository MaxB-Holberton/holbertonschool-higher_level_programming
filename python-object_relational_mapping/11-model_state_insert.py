#!/usr/bin/python3
"""
    Module for connecting to MySQL and grabbing states
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def run_database():
    engine = create_engine('mysql+mysqldb://{}:\
        {}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    print(new_state.id)


if __name___ = '__main__':
    run_database()
