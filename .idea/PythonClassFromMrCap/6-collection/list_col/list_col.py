# items = []               ###Cheking data type
# dt_it = type(items)
# print(dt_it)

items = ['John', 23, 234.89, 'John', True, [23,'Ola',False]]
dt_it = type(items)

items[3]= 'Paul'
print(items)

print(items[4])
print(items[2])

foods = list()
foods.append('Paul')
foods.append('John')
foods.append(234)
foods.append(234.9876)
foods.append([12, 'RAT', False])
print(foods)