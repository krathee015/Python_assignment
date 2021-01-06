print("Exercise 3")
# Write a program to handle an error if the user entered a number more than four digits it should
# return “The length is too short/long !!! Please provide only four digits” 
try:
    num = int(input("enter four digits number: "))
    if len(str(num)) != 4:
        raise ValueError
except ValueError:
    print("The length is too short/long !!! Please provide only four digits")
