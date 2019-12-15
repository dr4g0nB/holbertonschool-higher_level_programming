#!/usr/bin/python3
# Takes in an arg and displays all values in the states table of hbtn_0e_0_usa

import MySQLdb
import sys

# Doesn't execute when imported
if __name__ == "__main__":
    # Connects to a MySQL server
    db = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3],
                        #name=sys.argv[4]
                        )
try:
    # Performs a query
    crsor = db.cursor()
    crsor.execute("SELECT * FROM states WHERE name=%(name)s ORDER BY states.id ASC", {'name':sys.argv[4]} )
    fetch_all = crsor.fetchall()

    # To traverse the rows
    for row_db in fetch_all:
        print(row_db)
finally:
    # Close
    crsor.close()
    db.close()
