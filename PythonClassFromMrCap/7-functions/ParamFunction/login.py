user_name = 'Douglas Bankz'
password = 'abcd1234'
name = 'Douglas'

def login(user_name:str, password:str, name:str):
    if user_name == 'Douglas Bankz' and password == 'abcd1234':
        print(f'Welcome Mr {name}!!!, you are welcome to our WEBSITE')
    else:
        print('Check login details')   
        

login('Douglas Bankz','abcd1234', 'Douglas')         
    