animls = dict(one ='Rabbit', two = 'Dog', Three = 'Cat', four ='Lion',five = 'Tiger')

res = animls.items()
print(res)

for i, ii in res:
    print(f'The key is {i} and the value is {ii}')
    
res1 = animls.values()
print(res1)

tup_res = tuple([res1])    
res2 = str(tup_res).upper()
print(res2)  




    
    
    
    
