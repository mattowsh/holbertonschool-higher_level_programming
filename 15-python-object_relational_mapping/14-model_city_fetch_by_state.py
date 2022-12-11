#!/usr/bin/python3
"""
Task 14: prints all City objects from the database hbtn_0e_14_usa.
You must use the module SQLAlchemy
"""

import sys
import MySQLdb
from model_state import Base, State
from model_city import City
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_dbname = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        mysql_username, mysql_password, mysql_dbname))
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id).all()

    for state, city in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
