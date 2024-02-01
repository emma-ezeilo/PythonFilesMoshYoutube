 # Local variables ; these are variables found inside block-statements
 # e.g if, while, for, function, these are block-statement
 # Global variables
 
 
# name = 'jimi'      ### Globa variables

# if name == 'jimi':
#     age = 33           ### Local variables
#     salary = 344546
    

balance = 0.0
def save_money(amount:float):
    global balance
    balance = balance + amount
    print(balance) 
    
def withdraw_money(amount:float):
    global balance
    balance = balance - amount
    return amount

def show_bal():
    global balance
    print(balance)   
    
    
save_money(30000)
with_money = withdraw_money(8000)
print(with_money) 
show_bal()   