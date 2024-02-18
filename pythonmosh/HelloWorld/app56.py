# Exceptions
age = int(input("Age: "))
print(age)

# Giving an input of string will cause this program to give an error
# But we can add an exception (make it to print sth else without giving an exit code 1 error

try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("Invalid Value")
