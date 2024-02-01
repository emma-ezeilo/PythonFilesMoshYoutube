# This is a program that removes duplicates from a list for me
# This is wrong
numbers = [5, 6, 5, 3, 4, 8, 9]
duplicate = 0
for x in numbers:
    if numbers.count(x) > 1:
        x = duplicate
        print("It is a duplicate")
    else:
        print("It is not a duplicate\n ")

# Mosh's answer 2:13:27
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)