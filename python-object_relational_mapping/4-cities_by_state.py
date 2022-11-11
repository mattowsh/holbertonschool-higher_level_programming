#!/usr/bin/python3
"""
Task 4: lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    mysql_username = sys.argv[1]
    mysql_pwd = sys.argv[2]
    mysql_dbname = sys.argv[3]

    my_db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        password=mysql_pwd,
        db=mysql_dbname)

    qry_cursor = my_db.cursor()
    qry_cursor.execute("""SELECT c.id, c.name, s.name
                        FROM cities c LEFT JOIN states s
                        ON c.state_id = s.id
                        ORDER BY c.id ASC""")
    records = qry_cursor.fetchall()

    for element in records:
        print(element)

    my_db.close()
