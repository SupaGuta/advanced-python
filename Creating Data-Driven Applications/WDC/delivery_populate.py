"""This module inserts product data into the delivery database."""

from sqlite3 import connect

conn = connect("delivery.db")
cursor = conn.cursor()

query = "INSERT INTO products (prod_name, price) VALUES (?, ?)"
vals = [("Lumber – 2×4×96 inch", 5.50),
        ("Lumber – 2×6×96 inch", 8.50),
        ("Lumber – 2×4×96 inch (Treated)", 8.75),
        ("Lumber – 2×6×96 inch (Treated)", 13.25),
        ("Plywood – 1/4×48×96 inch", 33.00),
        ("Plywood – 1/2×48×96 inch", 37.25),
        ("Plywood – 1/2×48×96 inch (Particleboard)", 19.25)]

cursor.executemany(query, vals)

conn.commit()
conn.close()

print(f"{cursor.rowcount} record(s) inserted into the products table.")