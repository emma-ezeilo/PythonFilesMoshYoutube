# This is to check (or find) the maximum number in a list a Mosh assignment
# This is mosh answer i did not try it
numbers = [3, 9, 7, 10, 5]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

# I created the one for a 2d list
list_2d = [
    [2, 3, 4],
    [5, 3, 7],
    [6, 8, 9]
]
maximum = list_2d [0][0]
for numbera in list_2d:
    for numberb in numbera:
        if numberb > maximum:
            maximum = numberb
print(maximum)