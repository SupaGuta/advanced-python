import pandas as pd
import matplotlib.pyplot as plt

orders = pd.read_csv("orders_clean.csv")
totals_by_month = orders.groupby(["Order Month"]).sum()

months = orders["Order Month"].unique()
sales = totals_by_month["Sales"]

fig = plt.figure()
ax = fig.subplots(1, 1)
ax.bar(months, sales)
plt.show()