#!/usr/bin/python3
"""
Task 11: adds the State object “Louisiana” to the database hbtn_0e_6_us.
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

    # Create the new object = new record:
    new_state = State()
    new_state.name = "Louisiana"

    # Adding objects to the session doesn't actually writes them to the
    # database, it only prepares the objects to be saved in the next commit:
    session.add(new_state)

    # Now yes, we will finally add the new object.
    # add_all() method accepts a list of objects to be added to the session:
    session.add_all([new_state])

    # Save the objects to the database call commit() method:
    session.commit()

    # Makes the request and print the records :)
    result = session.query(State).filter(
        State.name == new_state.name).first()

    print(result.id)

    session.close()
