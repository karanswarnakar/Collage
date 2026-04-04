user = {
    "name": "Karan Swarnakar",
    "age": 20,
    "course": "BCA",
    "section": "C"
}

# Insert a New Element
user["city"] = "Kolkata"

# Modify an element
user["course"] = "BCA(H)"

# Delete Element 
del user["section"]


print(user)
# List of KEYS Print
for i in user:
    print("Key: " + i)
print(" ")
# List of Values Print
for i in user:
    print("Value: ",user[i])


# Return Keys 
keys_of_user = list(user.keys())
print(keys_of_user)


# Return Values 
values_of_user = list(user.values())
print(values_of_user)
