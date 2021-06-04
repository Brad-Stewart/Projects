# OOP - Object Oriented Programming
# Four Pillars of OOP
# 1. Encapsulation
# 2. Abstraction
# 3. Inheritance
# 4. Polymorphism


# CLASSES
class ClassName:
    def __init__(self):
        self.something="something"
    def something(self)
# DEFINE
class Dog: # SINGULAR AND UPPER CAMEL CASE
    def __init__(self, nameParam, legsParam, eyesParam, furParam): # CONSTRUCTOR METHOD
        #EVERY SINGLE CLASS NEEDS TO START WITH THE DUNDER INIT (__init__)
        # ATTRIBUTES (things that make up somethings)
        print("YOU ARE CREATING A NEW DOG")
        self.name = nameParam
        self.legs = legsParam
        self.eyes = eyesParam
        self.fur = furParam
        self.bark()

# METHODS (things you can do with attributes, actions)
    def bark(self):
        print(f"Hi my name is {self.name}")

    def play(self):
        print(f"{self.name} played in the mud")
        self.fur = "dirty"


    def__repr__(self):
        return f" {self.name}, {self.legs}"

# INSTANTIATE
dog1 = Dog("Spot", 4, "brown", "soft") # NEEDS TO BE STORED INSIDE A VARIABLE (DOG1)
dog1.bark()
dog1.play()
print(dog1.fur)

dog2 = Dog("Rover", 4, "black", "mangy")
dog2.bark()

print(dog2.name)
dog3.bark()