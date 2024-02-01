my_greet = 'CONGRATULATE'
st_res = my_greet.startswith('C')
print(st_res)

rep_res = my_greet.replace('CON','pre')
print(rep_res)

alp_res = my_greet.isalpha()
print(alp_res)

cap_res = my_greet.capitalize()
print(cap_res)

my_sch = 'SPRING GRATE SCHOOL'
low_res = my_sch.lower()
print(low_res)

my_name = 'MR EZEKIEL CHUKS'
tit_res = my_name.title()
print(tit_res)

my_txt = 'myLIFE is imPorTaNt'
sw_res = my_txt.swapcase()
print(sw_res)

name = 'John'
age = '22'
info = 'My name is {} and my age is {}'.format(name,age)
print(info)

info2 = 'My state is {state} and my salary is {salary}'.format(state ='Imo', salary = '419000')
print(info2)

val = 'Lagos'
res = val.center(30)
print(res)

res2 = val.center(30,'*')
print(res2)