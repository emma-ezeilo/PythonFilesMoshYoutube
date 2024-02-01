my_matric_num = 22334455
her_gender = "Female"
her_height = 5.7
his_salary : float = 345_000_000.0
is_married = False

### string casting ######
str_cast = str(my_matric_num)
print(str_cast)

## checking data type ##
ty_res = type(str_cast)
print(ty_res)

## checking varible address ##
str_res = str_cast * 2
print(id(str_cast))
print(id(str_res))

str_cast1 = str(her_height) ## casting data type
print(str_cast1)

ty_res1 = type(str_cast1) # checking data type###
print(ty_res1)

str_cast2 = str(his_salary) ## casting data type ##
print(str_cast2)

ty_res2 = type(str_cast2)  # checking data type###
print(ty_res2)

str_cast3 = str(is_married)  ## casting data type ###
print(str_cast3)

ty_res3 = type(str_cast3)   # checking data type###
print(ty_res3)