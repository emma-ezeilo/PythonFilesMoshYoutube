def greet_user(name):
    print(f"Hi {name} !")
    print("Welcome aboard")


# We can also do this
print("start")
greet_user("John")
greet_user("Mary")
print("Finish")

# This will give an error
print("start")
greet_user()
print("Finish")