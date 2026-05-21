import matplotlib.pyplot as plt
import numpy as np

students = ["A", "B", "C", "D", "E","F", "G", "H","I","K"]
study_hours = np.random.randint(1,5,10)

math = np.random.randint(1,100, 10)
english = np.random.randint(1,100, 10)
science = np.random.randint(1,100, 10)



plt.bar(students, study_hours)
plt.show()
