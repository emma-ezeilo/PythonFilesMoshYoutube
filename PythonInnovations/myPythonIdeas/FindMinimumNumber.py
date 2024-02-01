# Program to find minimum number with python
while True:
    number_list = int(input("Please separate with commas\nType in the numbers: "))
    if number_list == finish:
        break
number = [number_list]
min_number = int([0])
for min in number:
    if min < min_number:
        number = min
print(min)
