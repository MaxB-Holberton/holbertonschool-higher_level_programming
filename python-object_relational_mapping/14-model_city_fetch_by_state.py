#!/usr/bin/python3
"""
    Module for connecting to MySQL and grabbing states
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def run_database():
    """
        Function to connect to the database and perform the sort
    """
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])
    engine = create_engine(url)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = (session.query(State, City)
    .join(City, State.id == City.state_id)
    .order_by(City.id)
    .all())

    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()


if __name__ == '__main__':
    """
        the main function
    """
    run_database()
