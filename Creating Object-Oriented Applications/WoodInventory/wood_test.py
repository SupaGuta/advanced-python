"""This module imports the Wood and Plywood classes and tests them."""

from wood import Wood, Plywood

plywood1 = Plywood("Plywood – 1/4 inch", "Sanded", 33.00, 20)
plywood2 = Plywood("Plywood – 1/8 inch", "Rough", 27.00, 25)

if plywood1 == plywood2:
    print("Both products cost the same.")
elif plywood1 > plywood2:
    print(f"{plywood1.product} is more expensive than {plywood2.product}.")