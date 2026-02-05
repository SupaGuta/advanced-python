"""This module retrieves info from an inventory database."""

from sqlite3 import connect

conn = connect("inventory.db")
cursor = conn.cursor()

# Describe the inventory table fields.
query = "PRAGMA table_info([inventory])"
cursor.execute(query)

print(cursor.fetchall())

# Print the inventory table fields.
query = "SELECT * FROM inventory"
cursor.execute(query)

records = cursor.fetchall()

for record in records:
    print(record)

conn.close()