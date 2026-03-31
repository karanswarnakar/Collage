# write a Python program to plot a histogram for randomly
# generated data.
import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(50,10,100)
plt.hist(data,bins=10,color="red",edgecolor="black")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()