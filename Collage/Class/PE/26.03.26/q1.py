# Create a bar chart to show number of boys and girls in four classes label,title and legend.
import matplotlib.pyplot as plt
boys = [18,25,22,24]
girls = [18,20,19,23]
classes = ["Class1","Class2","Class3","Class4"]

plt.bar(classes,boys,label="Boys")
plt.bar(classes,girls,bottom=boys,label="Girls")

plt.xlabel("Classes")
plt.ylabel("Number of Students")
plt.title("Number of Boys and Girls in defferent Classes")
plt.legend()
plt.show()