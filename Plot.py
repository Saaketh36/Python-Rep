import matplotlib.pyplot as plt

data = [10, 20, 20, 30, 30, 30, 40, 50]

plt.hist(data, bins=5)
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()