items = ('John', 23, 234.89, 'John', True, [23,'Ola',False])
dt_it = type(items)
print(dt_it)
print(items)
print(items[0:4])

#### adding items into a tuple constructor ####

names = tuple(['John','Paul','James'])      ## using list
print(names)


fruits = tuple('Pine Apple')         ## using string


countries = tuple(('Mali','Togo','Benin','Niger'))   ## using tuple