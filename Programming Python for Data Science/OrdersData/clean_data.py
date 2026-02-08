import pandas as pd

orders = pd.read_csv("orders.csv")

orders.drop(columns=["Shipping Method"], inplace=True)

orders["Profit"] = orders["Sales"] - orders["COGS"]

orders[["First Name", "Last Name"]] = \
orders["Customer Name"].str.split(" ", expand=True)
orders.drop(columns=["Customer Name"], inplace=True)

orders.sort_values(["Order Month", "Last Name", "First Name"], inplace=True)

print(orders)
orders.to_csv("orders_clean.csv")