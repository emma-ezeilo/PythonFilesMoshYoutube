'''
There are four ways to print data in python
1, String concatenation method
2, f-string method
3, String format method
4, Old format method 

'''




my_name = 'Kola'
my_age = '23'
my_gender :str = 'Male'
my_salary : '40000000'
print('my gender is '+ my_gender)
print('My name is '+ my_name+' my age is '+ my_age)
my_name : str = 'Kola'
my_age : int = 23
my_gender : str 
my_salary : float = 'Male' , 40000000
my_state = None
my_state = 'Imo'

''' f-string Method'''
my_dog_name = 'Clinton'
its_breed = 'Rothweiler'
print(f'My dog name is {my_dog_name} its breed is {its_breed}')

'''format-string Method'''
my_dog_name1 = 'Clinton'
its_breed2 = 'Rothweiler'
print('My dog name is {0} its breed is {1}'.format(my_dog_name1,its_breed2))

'''Old format Method'''
my_dog_name2 = 'Clinton'
its_breed3 = 'Rothweiler'
print('My dog name is %s its breed is %s %(my_dog_name2,its_breed3 ) ')