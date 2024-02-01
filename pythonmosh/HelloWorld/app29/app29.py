full_name = input("Your full name: ")

# For Emma This is the code I will write for the database form of a name input tab (Just Know it is backend)
# Even though it is a class project
if len(full_name) < 3:
    print("Name must be at least 3 characters: ")
elif len(full_name) > 50:
    print("Name can only be a maximum of 50 characters: ")
else:
    print(full_name)
    print("Name is Good: ")
