# Write a program in Python to find out the character in a string which is uppercase using list
# comprehension

upper_char = [word for word in "comPreHensioN" if word.isupper() == True]
print("Uppercase characters in the string: ",upper_char)