# Exercise on they want us to define a new type called person.
# This person will have name attributem and a talk() method
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print("I am talking")


john = Person("JohnSmith")
john.talk()
print(john.name)
#Now we can make it better with formatted string in the class
class Person2:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person2("John Smith")
john.talk()