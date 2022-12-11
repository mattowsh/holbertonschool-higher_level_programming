#!/usr/bin/python3
"""
Task 12: changes the name of a State object from the database hbtn_0e_6_usa.
You must use the module SQLAlchemy
"""

import sys
import MySQLdb
from model_state import Base, State
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

    result = session.query(State).filter(State.id == 2).update(
        {"name": "New Mexico"}, synchronize_session='fetch')
    session.commit()
    # Also, I would take the object with id == 2 and update his name attribute:
    # ej. filter State.id.like(2) and result.name = "New Mexico"

    session.close()
