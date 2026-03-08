#!/ussr/bin/python3
"""
    Module for connecting to MySQL and grabbing states
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def run_database():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    searched_state = session.query(State).filter(State.id == 2)
    searched_state.name = 'New Mexico'
    session.commit()

    session.close()


if __name___ = '__main__':
    run_database()
