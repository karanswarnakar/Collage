# Using Seaborn, NumPy, and Matplotlib, write a Python program to plot a Kernel Density Estimation (KDE) graph
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data = np.random.normal(50,10,100)
sns.kdeplot(data, fill=True)
plt.xlabel("Values")
plt.xlabel("Density")
plt.title("KDE Plot")
plt.show()