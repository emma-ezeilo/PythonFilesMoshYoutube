name = input('Please enter your name >>> ').lower().strip()

match name:
    case "john":
        print('My name is John')
    case "peter":
        print('My name is Peter')   
    case 'paul':
        print('My name is Paul')  
    case _ :
        print('Please enter the correct name')       

