full_name = int(input("Your full name: "))

# It is giving me error so check app29.py for answer of this program

if full_name < 3:
    print("Name must be at least 3 characters: ")
elif full_name > 50:
    print("Name can only be a maximum of 50 characters: ")
else:
    print(full_name)
    print("Name is Good: ")
