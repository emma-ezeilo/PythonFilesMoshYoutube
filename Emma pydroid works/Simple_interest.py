principal = int(input("please enter the principal amount: "))
rate = int (input("please enter the rate in %: "))
time = int(input("please enter the time in yrs: "))
interest = int((principal*rate*time)/100)
print(round(interest, 2))
