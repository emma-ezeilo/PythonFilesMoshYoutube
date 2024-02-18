# Inheritance
class Mammal():
    def walk(self):
        self.walk()
        print("walk")


class Dog(Mammal): # Inheritance is used when two or more classes have sth in common .To avoid dry we put their similarities in a class with a featuristic name e.g dog and cat can walk and they are mammals so to avoid dry we did what we did in the code
    pass # We use the pass keyword to tell pycharm to not care about there being no function or code in the class


class Cat(Mammal):
    pass # We use the pass keyword to tell pycharm to not care about there being no function or code in the class


