import matplotlib.pyplot as plt 
import numpy as np

students = ["A", "B", "C", "D", "E","F", "G", "H","I","K"]
math = np.random.randint(1,100,10)

plt.scatter(students, math, marker="+" ,color='red')
plt.show()