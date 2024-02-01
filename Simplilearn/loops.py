# While loops
# Program to check whether a number is a multiple of 7
val = int(input("Enter a number: "))

while val % 7 != 0:
    val = int(input("Enter a number: "))
else:
    print("Is a multiple of 7")