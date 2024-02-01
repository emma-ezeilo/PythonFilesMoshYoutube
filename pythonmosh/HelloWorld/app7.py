'''this code prints out your age at 2023 and prints out the type of some variables at any instant '''
birth_year= input("Type in your Birth year: ")
print(type(birth_year)) # It was a string here
age = 2023 - int(birth_year)
print(type(age)) #Now it is an integer
print(age)

"""This is an updated version that is for any year"""

answer = input("Do you want to try the next program (If yes Type Y if no Type N): ")
if answer.lower() == "y":
    birth_year = input("Type in your Birth year: ")
    current_year = input("Type in your current_year: ")
    age = int(current_year) - int(birth_year)
    print(age)

elif answer.lower() == "n":
    print("Thank You")

else:
    print("You didn't type y/n")