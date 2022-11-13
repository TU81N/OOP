class Cat():
    def __init__(self, name, colour):  # __init__ is the constructor that is responsible for creating an instance
        self.name = name  # self refers to the current instance we are handling
        self.colour = colour
        self.intelligence = 10
        self.weight = 5
        self.energy = 50

    def make_noise(self):
        print("Meow!")
        print("My name is " + self.name)

    def eat(self, food):
        print(self.name + " will now be fed " + food)
        self.weight += 1
        self.energy += 10
        print(self.name + " now has a weight of " + str(self.weight))
        print(self.name + " now has an energy level of " + str(self.energy))

kuro = Cat('Kuro', 'Black')  # this is called an instance (a specific occurence of a class)
randy = Cat('Randy', 'Ginger')

kuro.eat("fish")
randy.eat("milk")

#Basics of OOP