 #!/usr/bin/python3
"""
Task 7: script that lists all State objects from the database hbtn_0e_6_usa.
You must use the module SQLAlchemy
"""

import sys
import MySQLdb
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import create_engine, sessionmaker


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
    results = session.query(State).all()

    for element in results:
        print("{}: {}".format(element.id, element.name))

    session.close()
