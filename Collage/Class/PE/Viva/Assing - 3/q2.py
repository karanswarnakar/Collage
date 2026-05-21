import matplotlib.pyplot as plt 
import numpy as np

students = ["A", "B", "C", "D", "E","F", "G", "H","I","K"]
study_hours = np.random.randint(1,5, 10)
math = np.random.randint(1,100,10)
plt.scatter(students, math, marker="+" ,color='red')
plt.show()