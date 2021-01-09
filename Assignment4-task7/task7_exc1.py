# Write a program that calculates and prints the value according to the given formula:
# Q= Square root of [(2*C*D)/H]
import math

C = 50
H = 30
class SquareRoot:
    def __init__(self,values):
        self.values = values
    def calculate(self):
        self.values = self.values.split(',')
        conv = map(int,self.values)
        result = []
        for D in conv:
            Q= math.sqrt((2*C*D)/H)
            result.append(Q)
        return result

values = input("Enter value of D in comma seperated: ")
sr = SquareRoot(values)
print(sr.calculate())






