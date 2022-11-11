#!/usr/bin/python3
"""
Task 0: lists all states from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    mysql_username = sys.argv[1]
    mysql_pwd = sys.argv[2]
    mysql_dbname = sys.argv[3]

    # to connect my target db: establish the connector:
    my_db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        password=mysql_pwd,
        # db I want to connect to:
        db=mysql_dbname)

    # to execute the query of interest --> my SQL request:
    qry_cursor = my_db.cursor()

    sql_request = "SELECT * FROM states ORDER BY id ASC"
    qry_cursor.execute(sql_request)

    # fetchall statement selects all data from the state table:
    records = qry_cursor.fetchall()

    # print all records:
    for element in records:
        print(element)

    my_db.close()
