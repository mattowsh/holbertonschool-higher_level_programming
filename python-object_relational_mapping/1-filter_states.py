#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import MySQLdb

    mysql_username = sys.argv[1]
    mysql_pwd = sys.argv[2]
    mysql_dbname = sys.argv[3]

    my_db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username
        password=mysql_pwd
        db=mysql_dbname)

    qry_cursor = my_db.cursor()
    sql_request = "SELEC * FROM states WHERE state LIKE BINARY 'N%'"
    qry_cursor.execute(sql_request)
    records = qry_cursor.fetchall()

    for element in records:
        print(element)

    my_db.close()