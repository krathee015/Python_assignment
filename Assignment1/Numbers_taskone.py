print ("Question 1: Create three variables in a single line.")
num , flt , str = 123, 2.5, "KR"

print("\n")
print("**********")
print(" 2. Create a variable of type complex and swap it with another variable of type integer.")
com = 2+2j
var1 = 223

com, var1 = com, var1

print ("After swaping the variable of type integer will be: ", com, var1)

print("\n")
print("**********")
print ("3. Swap two numbers using a third variable and do the same task without using any third variable.")

#3.a. first doing using three variables

num1 = 10
num2 = 20
temp = 0

temp = num1
num1 = num2
num2 = temp

print ("After swapping using temp as a variable: ", num1,num2)

#3.b. without using third variable 

a = 2
b = 4
a , b = b , a

print ("After swapping without third variable: ", a,b)

print("\n")
print("**********")
print("4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.xVersion.")

#pyth2 = raw_input("Enter the input: ")
pyth3 = input("Enter the input: ")

print("\n")
print("**********")
print("5. Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum inanother variable called z. ")

print ("Kindly add two numbers between 1-10")
x = eval(input("Enter first number: "))
y = eval(input("Enter second number: "))
z = x + y
result = z + 30

print ("the final result is: ",result)

print("\n")
print("**********")
print ("6. Write a program to check the data type of the entered values.")
data_type = eval(input("Enter any value to check data type: "))
print (type (data_type))

print("\n")
print("**********")
print("7. Create Variables using formats such as Upper CamelCase , Lower CamelCase , SnakeCase and UPPERCASE.")

upper_camelcase = "KanikaRathee"
lower_camelcase = "kanikaRathee"
snake_case = "kanika_rathee"
upper_case = "KANIKA RATHEE"
print ("Upper camel case: ",upper_camelcase)
print ("lower camel case: ",lower_camelcase)
print ("snake case: ",snake_case)
print ("upper case: ", upper_case)

print("\n")
print("**********")
print ("8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’again. ")

a = 34
a = "KR"

print (a)

#yes, as the value of a got updated to latest one



