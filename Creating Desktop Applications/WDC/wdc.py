"""This module creates an interface for ordering
products from Woodworkers Wheelhouse."""

from tkinter import (Tk, Frame, Button, Entry, Label,
                     Menu, Radiobutton, StringVar, END)

class Application(Frame):
    """Creates the application window."""

    def __init__(self, master):
        """Construct class instance with product data."""
        super().__init__(master)
        self.grid()
        self.products = ["Lumber – 2×4×96 inch",
                         "Lumber – 2×6×96 inch",
                         "Lumber – 2×4×96 inch (Treated)",
                         "Lumber – 2×6×96 inch (Treated)",
                         "Plywood – 1/4×48×96 inch",
                         "Plywood – 1/2×48×96 inch",
                         "Plywood – 1/2×48×96 inch (Particleboard)"]
        self.prices = [5.50, 8.50, 8.75, 13.25, 33.00, 37.25, 19.25]
        self.ship_days = {"1 day": 20.00, "2 days": 15.00, "3 days": 10.00}

        self.create_widgets()
