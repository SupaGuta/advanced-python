"""This module provides various services to the
Wood Delivery Calculator client app using the delivery database."""

from sqlite3 import connect
from decimal import Decimal
from datetime import date
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

# Create the Flask app and API objects.



class Products(Resource):
    """Gets product data from products table."""

    def get(self):
        """Get product data."""
        self.conn = connect("delivery.db")
        self.cursor = self.conn.cursor()

        self.products = []
        self.cursor.execute("SELECT prod_name FROM products")
        self.row = self.cursor.fetchall()
        for row in self.row:
            self.products.append(row[0])
        self.conn.close()

class Prices(Resource):
    """Gets prices data from products table."""

    def get(self):
        """Get prices data."""
        self.conn = connect("delivery.db")
        self.cursor = self.conn.cursor()

        self.prices = []
        self.cursor.execute("SELECT price FROM products")
        self.row = self.cursor.fetchall()
        for row in self.row:
            self.prices.append(Decimal(row[0]))
        self.conn.close()