#!/usr/bin/python3
"""
Task 5: takes in the name of a state as an argument and lists all cities of
that state, using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    mysql_username = sys.argv[1]
    mysql_pwd = sys.argv[2]
    mysql_dbname = sys.argv[3]
    mysql_tomatch = sys.argv[4]

    my_db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        password=mysql_pwd,
        db=mysql_dbname)

    qry_cursor = my_db.cursor()
    qry_cursor.execute("""SELECT c.name
                        FROM cities c LEFT JOIN states s
                        ON c.state_id = s.id
                        WHERE s.name LIKE BINARY '{}'
                        ORDER BY c.id ASC""".format(mysql_tomatch))
    records = qry_cursor.fetchall()

    for i, element in enumerate(records):
        if i != 0:
            print(", ", end="")
        print(element[0], end="")
    print()

    my_db.close()
