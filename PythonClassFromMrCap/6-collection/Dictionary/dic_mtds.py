countries = dict()
countries.update(ng = 'Nigeria', gh = 'Ghana', bn = 'Benin')
countries.setdefault('sa', 'South Africa')

print(countries)

res_get = countries.get('ng')
print(res_get)

pop_res = countries.pop('bn')
print(pop_res)

key_res = countries.keys()
print(key_res)

values_res = countries.values()
print(values_res)

countries.clear()
