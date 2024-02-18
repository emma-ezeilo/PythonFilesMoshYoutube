# Inheritance 2
class Mammal():
    def walk(self):
        self.walk()
        print("walk")


class Dog(Mammal):
    def bark(self):
        self.bark()
        print("bark") # Once there is any function in the class no need for the pass keyword


class Cat(Mammal):
    def hiss(self):
        self.hiss()
        print("Meooooow!")


# Now we can call them
dog1 = Dog()
dog1.bark()