import random
# This is imports the random module
for i in range(3):
    print(random.random())
    # This produces 3 random floating point numbers


print("\n")
# But to create for integers we use .randint
for j in range(5):
    print(random.randint(10, 20))
    # This produces 5 values of random numbers between 10 to 20

