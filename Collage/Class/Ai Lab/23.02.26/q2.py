l = []
for i in range(0,5,1):
    n = int(input("Enter number: "))
    l.append(n)
for i  in range(0, 4, 1):
    if(l[i] > l[i+1]):
        maxValue = l[i]
    else: 
        maxValue = l[i+1]
print("Max Value: ", maxValue)