#here we are using the find() method to bring back the index of the characters we want
''' course = 'Python for Beginners'
print(course.find(input("Type what you are looking for ")))
I thought of this code '''
course='Python for Beginners'
print(course.find('P'))
print(course.find('O'))# this will print out -1
# WE can also use the replace() method to replace a string to do this we use the comma and type the replacer on the right
# side of the comma and what is being replaced on the left side
print(course.replace('Beginners', 'Absolute Beginners'))
# The output is Python for Absolute Beginners
# if you make a mistake in 'Beginners' you will get Python for Beginners
print(course.replace('beginners', 'Absolute Beginners'))