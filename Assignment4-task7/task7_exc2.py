# Define a class named Shape and its subclass Square. The Square class has an init function which
# takes length as argument. Both classes have an area function which can print the area of the shape
# where Shape’s area is 0 by default.

class Shape:

    def area(self):
        self.area_var = 0
        print("area of shape is: ",self.area_var)

class Square(Shape):
    def __init__(self,length):
        self.length = length
    
    def area(self):
        area = (self.length * self.length)
        print("The area of square with length {} is:{}".format(self.length,area))

value_length = int(input("Enter the value of length: "))
s_shape = Shape()
s_shape.area()
s_square = Square(value_length)
s_square.area()

