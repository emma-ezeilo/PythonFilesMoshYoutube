countries = list()
countries.append('USA')
countries.append('UK')
countries.append('Canada')
countries.append('Germany')
countries.append('Spain')
countries.append('Australia')
print(countries)

###### list looping #####
for country in countries:
    print(country)
    
###### list slicing #####
slice_country = countries[1:4]    
print(slice_country)

slice_country2 = countries[-5:-2]
print(slice_country2)
