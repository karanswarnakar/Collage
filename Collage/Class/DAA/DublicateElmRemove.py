a = [1,2,4,4,5,8,9,2,8,50,4,5,7,1,7,0]
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)