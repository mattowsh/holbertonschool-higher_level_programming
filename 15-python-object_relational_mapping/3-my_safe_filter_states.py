#!/usr/bin/python3
"""
Task 3: takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument but safe from MySQL injections!
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
    qry_cursor.execute("""SELECT *
                        FROM states
                        WHERE name LIKE %s
                        ORDER BY id ASC""", (mysql_tomatch,))
    records = qry_cursor.fetchall()

    for element in records:
        print(element)

    my_db.close()
