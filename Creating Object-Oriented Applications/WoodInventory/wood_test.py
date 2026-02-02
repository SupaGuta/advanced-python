"""This module imports the Wood and Plywood classes and tests them."""

from wood import Wood, Plywood

# Create instances of the Wood and Plywood classes.
wood1 = Wood("Lumber – 2×4 inch", "Untreated", 5.50, 10)
plywood1 = Plywood("Plywood – 1/4 inch", "Sanded", 33.00, 10, 48, 96)

# Display the Wood and Plywood instance values.
wood1.display()
plywood1.display()

# Sell three pieces of wood and display the results.
wood1.sell_wood(3)
wood1.display()

# Change plywood width to 24 inches and display the results.
plywood1.width = 24
plywood1.display()