print ("Exercise 1")
print ("If a number is divisible by 3 it should print “Consultadd” as a string.")
print("If a number is divisible by 5 it should print “Python Training” as a string")
print("If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a string.")
print("\n")
num = eval(input("Enter the number: "))
if (num %3 == 0):
    print ("Consultadd")
elif (num %5 == 0):
    print ("Python Training")
elif (num %3 ==0 and num %5 ==0):
    print ("Consultadd - Python Training")
else:
    print ("The number is neither divisible by 3 nor 5")
print()




