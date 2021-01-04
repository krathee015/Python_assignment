from functools import reduce 
# function that can receive two integral numbers in string form and compute their sum and print it in the console

def calsum(a,b):
    sum = int(a) + int(b)
    return sum
sum1 = reduce(calsum, ["10","20"])
print("Sum= ",sum1)