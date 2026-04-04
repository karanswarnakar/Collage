l = [1,2,3,3,4,4,5,5,6,6]
uniq = []

for i in l:
    if(i not in uniq):
        uniq.append(i)

print(uniq)