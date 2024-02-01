person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

print(person['first_name'])
print(person['last_name'])
per_age = person.get('age')
print(per_age)
