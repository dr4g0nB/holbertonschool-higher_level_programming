#!/usr/bin/python3
# Lists all states with a name starting with N from database hbtn_0e_0_usa

import MySQLdb
import sys

# Doesn't execute when imported
if __name__ == "__main__":
    # Connection to database server
    db = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3]
                        )

# Performs a query
crsor = db.cursor()
crsor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")

fetch_all = crsor.fetchall()

# To traverse the rows
for row_db in fetch_all:
    print(row_db)

# Close the cursor and database
crsor.close()
db.close()
