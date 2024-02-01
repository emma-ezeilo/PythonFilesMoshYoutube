fruits = dict(first = 'Apple', second = 'Water melon',third = 'Orange', fourth = 'Pine apple', fifth = 'Carrot')


for key, values in fruits.items():
    print(f'The key is {key} the value is {values}')
    
fruits['first'] = 'Banana'
print(fruits)

fruits.update(sixtth = 'Mango')
fruits.update(seventh = 'Grape')
fruits.update(eight = 'Papaya')
print(fruits)

res_len = len(fruits.values())
print(res_len)

res_sot = sorted(fruits.values())
print(res_sot)

res_sot2 = sorted(fruits.items())
print(res_sot2)

reversed(fruits.items())