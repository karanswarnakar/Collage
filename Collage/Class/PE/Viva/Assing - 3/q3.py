import matplotlib.pyplot as plt 
import numpy as np


math = np.random.randint(1,100,10)
english = np.random.randint(1,100,10)
science = np.random.randint(1,100,10)

avg = []

avg.append(sum(math)/len(math))
avg.append(sum(english)/len(english))
avg.append(sum(science)/len(science))

subject = ["Math", "English", "Science"]

plt.pie(avg, labels=subject)
plt.show()

