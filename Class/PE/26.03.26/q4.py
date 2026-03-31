# Using Matplotlib and NumPy, write a Python program to create a box plot for outlierdetection.

import matplotlib.pyplot as plt
import numpy as np

data  = np.random.normal(50,10,100)
plt.boxplot(data)
plt.xlabel("Dataset")
plt.ylabel("Values")
plt.title("Box Plot")
plt.show()