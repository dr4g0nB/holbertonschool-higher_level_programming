#!/usr/bin/python3
# Lists all cities from the database hbtn_0e_4_usa

import MySQLdb
import sys

if __name__ == "__main__":
    # Connects to a MySQL server
    db = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3],
                        )
    # Performs a query
    crsor = db.cursor()
    crsor.execute("SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")
    fetch_all = crsor.fetchall()

    # To traverse the rows
    for row_db in fetch_all:
        print(row_db)

    # Close
    crsor.close()
    db.close()
