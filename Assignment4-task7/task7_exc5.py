# Write a Person class with an instance variable “age” and a constructor that takes an integer as a
# parameter. The constructor must assign the integer value to the age variable after confirming the
# argument passed is not negative; if a negative argument is passed then the constructor should set
# age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance
# methods:

class Person:

    def __init__(self,age):
        self.age = age
        if self.age < 0:
            self.age = 0
            print("Age is not valid, setting age to 0")
    
    def yearPasses(self, addage):
        new_age = addage + self.age
        print(new_age)

    def amIOld(self):
        if self.age > 0 and self.age < 13:
            print("You are young")
        elif self.age >= 13 and self.age <= 19:
            print("You are a teenager")
        else:
            print("You are old")

for i in range(0,7):
    input_age = int(input("Enter the age: "))
    p = Person(input_age)
    p.amIOld()
input_addage = int(input("Enter the number to increase the age by: "))
p.yearPasses(input_addage)


        
