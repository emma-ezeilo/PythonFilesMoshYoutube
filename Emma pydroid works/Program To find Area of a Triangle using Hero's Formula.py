#To find Area of a Triangle using Hero's Formula
a = (input("Please enter side a: "))
b = (input("Please enter side b: "))
c = (input("Please enter side c: "))
s = int((a+b+c)/(2))
z = (s*(s)+s*(-a)+(s)+(-b)+(s)+(-c))
Area = ((z)**(1/2))
print(Area)
