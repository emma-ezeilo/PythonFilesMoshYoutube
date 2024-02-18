# Using Keyword Arguments
def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


print("start")
greet_user(last_name="Smith", first_name="John")
print("Finish")
"""If you notice even if we interchange their position they still give the order the function defined
It is like this because of Keyword Arguments
"""