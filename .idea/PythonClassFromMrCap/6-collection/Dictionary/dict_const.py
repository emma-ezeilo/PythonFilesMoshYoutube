employee = dict(name = 'John', age = 33, gender = 'Male')
print(employee.get('age'))
print(employee.get('gender'))

employee.update(salary = 234335.00)
employee.update(state = 'Lagos')
print(employee)

emp_keys = employee.keys()
print(emp_keys)

emp_values = employee.values()
print(emp_values)

emp_items = employee.items()
print(emp_items)

for k, v in employee.items():
    print(f'The key  is {k} and value is {v}')