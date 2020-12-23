print ("Exercise 2")

result = 0
num1 = eval(input("Enter first number: "))
num2 = eval(input("Enter second number: "))

user_enter = eval(input("Enter 1 for Addition, Enter 2 for Subtraction, Enter 3 for Division, Enter 4 for Multiplication, Enter 5 for Average: "))

if (user_enter == 1):
    result = num1 + num2
    print ("Addition of two numbers is: ")
elif (user_enter == 2):
    result = num1 - num2 
    print("Subtraction of two numbers is: ")
elif (user_enter == 3):
    result = num1 / num2
    print ("Division of two numbers is: ")
elif (user_enter == 4):
    result = num1 * num2
    print ("Multiplication of two number is: ")
elif (user_enter == 5):
    first = eval(input("Enter third number: "))
    second = eval(input("Enter fourth number: "))
    result = (num1 + num2 + first +second)/ 4
    print ("Average of four numbers is: ")
else:
    print("Kindly enter correct number 1-5")

if (user_enter <= 5 and user_enter > 0):
    print(result)

if (result < 0):
    print("Negative")    