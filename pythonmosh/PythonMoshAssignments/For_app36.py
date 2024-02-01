# Assignment on loops

numbers = [5, 2, 5, 2, 2]
for x in numbers:
    print("x" * x)
    # My answer is wrong because it is not in a for loop form but it still gives the same answer

numbers = [5, 2, 5, 2, 2]

for x_count in numbers:
    output = ''
    for count in range(x_count):
        print(count)
# I tried printing the answer at this point to try and understand it ( I also added print(count) in the code)

# Mosh answer
numbers = [5, 2, 5, 2, 2]

for x_count in numbers:
    output = ''     # Here the output is reset after each iteration
    for count in range(x_count):
        output += "x"  # From here I understood that he was adding x with the feature that loops Repeat and to do this he had to use an augmented operator += z
    print(output)
print('\nMosh Answer\n')

# Now for adventurism we are adjusting the values to get other letters e.g L
numbers = [2, 2, 2, 5]

for x_count in numbers:
    output = ''     # Here the output is reset after each iteration
    for count in range(x_count):
        output += "x"  # From here I understood that he was adding x with the feature that loops Repeat and to do this he had to use an augmented operator += z
    print(output)
