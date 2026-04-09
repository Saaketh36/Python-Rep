import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.DataFrame({
    "day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "sales": [200, 220, 250, 270, 300],
    "profit": [20, 25, 30, 35, 40]
})
# sn.histplot(data)
# sn.lineplot(data=data, x="day", y="sales")
# plt.title("Sales Trend")
# sn.lineplot(data=data, x="day", y="sales", label="Sales")
# sn.lineplot(data=data, x="day", y="profit", label="Profit")
# plt.title("Sales vs Profit")
# sn.histplot(data["sales"], kde=True)
# plt.title("Sales Distribution")
sn.pairplot(data)
plt.show()