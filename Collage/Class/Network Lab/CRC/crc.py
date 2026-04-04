def xor(a, b):
    res = ""
    l = min(len(a), len(b))
    for i in range(1, l):
        if a[i] == b[i]:
            res = res + "1"
        else:
            res = res + "0"
    return res

def crc(data, gen):
    m = len(gen)
    data2 = data + "0" * (m-1)
    temp = data2[0:m]
    while m<len(data2):
        if temp[0] == "1":
            temp= xor(gen,temp) + data2[m]
        else:
            temp= xor("0"*m,temp) + data2[m]
        m = m + 1
        if temp[0] == "1":
            temp= xor(gen,temp)
        else:
            temp= xor("0"*len(gen),temp)
        r = temp
        return r
# Sender
data = input("Enter Data: ")
gen = input("Enter Generator: ")

rem = crc(data, gen)
codeword = data + rem
print("Remainder Codeword: ", rem)
print("Codeword: ", codeword)

# Receiver
rdata = input("Enter Receiver Data: ")
check = crc(rdata, gen)
if int(rdata) == 0:
    print("No Error")
else:
    print("Error Detected!")
