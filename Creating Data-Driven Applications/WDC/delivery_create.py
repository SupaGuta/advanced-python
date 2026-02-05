"""This module creates the delivery database."""

from sqlite3 import connect

conn = connect("delivery.db")
cursor = conn.cursor()

# Create products table.
prod_query = """
	     CREATE TABLE products (
                 prod_name TEXT NOT NULL UNIQUE,
                 price NUMERIC NOT NULL
             )
             """

cursor.execute(prod_query)

print("The products table was created in the delivery database.")

# Create orders table.
orders_query = """
	       CREATE TABLE orders (
                   order_num INTEGER NOT NULL UNIQUE,
                   order_date TEXT NOT NULL,
                   ship_method TEXT NOT NULL,
                   total_price NUMERIC NOT NULL,
                   PRIMARY KEY(order_num AUTOINCREMENT)
               )
               """

cursor.execute(orders_query)
conn.close()

print("The orders table was created in the delivery database.")