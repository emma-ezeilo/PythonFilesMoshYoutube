input1 = input("Enter your weight: ")
input2 = input("Enter (L) to lbs or (K) to kgs: ")

if input2.lower() == 'l':
    weight_lb = float(input1) / 0.45
    print(weight_lb)

elif input2.lower() == 'k':
    weight_kg = float(input1) * 0.45
    print(weight_kg)

# Now to check if I am correct
# I am correct though I will get a 7 out of 10
# Mosh answer is in app30.py
else:
    print("You didn't type l or k")
