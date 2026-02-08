import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

orders = pd.read_csv("orders_clean.csv")

# Perform holdout method.
X = orders[["Sales"]]
y = orders["Profit"]
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Train linear regression model.
linreg = LinearRegression()
linreg.fit(X_train, y_train)

# Predict results on test set.
y_pred = linreg.predict(X_test)

results = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})
print(results)

# Visualize the linear regression model.
fig, ax = plt.subplots(1, 2)

ax[0].scatter(X_train, y_train, color="red")
ax[0].plot(X_train, linreg.predict(X_train))
ax[0].set_title("Training Set")
ax[0].set_xlabel("Sales")
ax[0].set_ylabel("Profit")

ax[1].scatter(X_test, y_test, color="red")
ax[1].plot(X_test, y_pred)
ax[1].set_title("Test Set")
ax[1].set_xlabel("Sales")
ax[1].set_ylabel("Profit")

# Predict profits from unseen sales figure.
unseen_sale = pd.DataFrame({"Sales": [157.00]})
unseen_pred = linreg.predict(unseen_sale)

fig, ax = plt.subplots()
ax.scatter(X_test, y_test, color="red")
ax.plot(X_train, linreg.predict(X_train))
ax.scatter(unseen_sale, unseen_pred, color="black", marker="X", s=100)
ax.set_title("Predicted Profit for $157 Sale")
ax.set_xlabel("Sales")
ax.set_ylabel("Profit")

plt.show()