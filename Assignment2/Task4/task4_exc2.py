print("Exercise 2")
print("Write a function that accepts a string and prints the number of uppercase letters and lowercase letters.")

input_str =input("Enter string containing lower and upper case characters: ")

def upper_lower(str1):
    no_of_upper = 0
    no_of_lower = 0

    for char in str1:
        if char.isupper():
            no_of_upper+= 1
        elif char.islower():
            no_of_lower+= 1
    print("No of upper case are: ", no_of_upper)
    print("No of lower case are: ", no_of_lower)
    
upper_lower(input_str)