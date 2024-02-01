nationality = input('Please Enter Your Nationality >>>> ').lower().strip()
age : int = int(input('Please enter your age >>> ').strip())

if nationality == 'nigerian':
    if age >= 18:
        print('You are eligible to vote in Nigeria')
    else:
        print('You can not vote because you are under age!!')    
else:
    print('You can not vote because you are not a Nigerian!!')        
        