# We are doing list methods here we are dealing on the operations we can perform on a list

numbers = [5, 2, 7, 1]
# We use .append() to add new items to a list
numbers.append(20)
print(f"{numbers}\n")

# If you notice the number is at the end of our list to make it at the beginning we use .insert()
numbers = [5, 2, 7, 1]
numbers.insert(0, 70)
# NB: the .insert() takes two values the index then the value you are inserting
print(f"{numbers}\n")

# We can also remove an item with .remove()
numbers = [5, 2, 7, 1]
numbers.remove(70)
# If the value in the .remove() is wrong it will display an error so the better way is
# Asking if the value is in the list first
print(20)



# If you want to remove all the items in the list we use the .clear()
numbers = [5, 2, 7, 1]
numbers.clear()
print(f"{numbers}\n")

# We use the .pop() to remove the last item in the list
numbers = [5, 2, 7, 1]
numbers.pop()
print(f"{numbers}\n")

# We use the .index() to know the index of an item
numbers = [5, 2, 7, 1]
numbers.index(5)
# But if the item is not in the list we get an error
# So it is better to use the in operator
print(50 in numbers)
# For this it will display false because 50 is not in the list

# # This code will check if an item is in the list NB: Ezeilo-Bernard Emmanuel Chisom created this
# numbers = [5, 2, 7, 1]
# searched_item = input("Type the item: ")
# if searched_item in numbers:
#     print(f"{searched_item} is in the list")
# else:
#     print(f"{searched_item} is not in the list")

# The .count() displays how many times an item occurred in a list
numbers = [5, 2, 7, 1, 5, 4]
print(numbers.count(5))
print("\n")
