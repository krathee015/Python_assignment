no_of_digits = 0
no_of_letters = 0

str = input ("Enter the alpha numeric value: ")
for num in str:
    if num.isalpha():
        no_of_digits += 1
    elif num.isdigit:
        no_of_letters += 1
    
print("Letters: ",no_of_letters)
print("Digits: ", no_of_digits)