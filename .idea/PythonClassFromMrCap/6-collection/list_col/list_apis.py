countries = list()
countries.append('USA')
countries.append('UK')
countries.append('Canada')
countries.append('Germany')
countries.append('Spain')
countries.append('Australia')

countries.extend(['France', 'Mali', 'Togo', 'Nigeria'])
countries.sort()                     ##### arranging in alphbetical oreder
countries.sort(reverse=True)          #### arranging 
countries.insert(1, 'Russia')
countries.remove('Togo')
# print(countries)

# ger_res = countries.pop(6)
# print(ger_res.lower())

# res = len(ger_res)
# print(res)

new_list = countries.copy()
print(new_list)
new_list.clear()
print(new_list)
