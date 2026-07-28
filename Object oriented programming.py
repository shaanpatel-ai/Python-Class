#Write a Python class named Rectangle with a length and width and a method that computes the area of a rectangle. Display the dimensions and calculated area of the rectangle as well.
class rectangle:
    def __init__(self,width,length):
        self.width=width
        self.length=length
    def area_of_the_rectangle(self):
        print("the width of the rectangle is",self.width)
        print("the length of the rectangle is",self.length,"cm")
        print("area of the rectangle is",self.width*self.length,"cm²")
v1=rectangle(10,8)
v1.area_of_the_rectangle()