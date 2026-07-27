#Write a program to create a class Parrot and perform the following tasks - Create a class variable species, Create a constructor that has instance variables - name and age, Create instances of class Parrot, passing arguments as well, Print Class variable by accessing it, Print Instance variables as well.
class parrot:
    species = "bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age
flappy = parrot("flappy",9)
birdy = parrot("birdy",10)
print("falppy is a {}".format(flappy.species))
print("birdy is a {}".format(birdy.species))
print("{} is {} years old".format(flappy.name, flappy.age))
print("{} is {} years old".format(birdy.name, birdy.age))