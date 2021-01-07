# Write a program in Python using generators to reverse the string.

def func(rev_str):
    length = len(rev_str)
    for i in range(length-1,-1,-1):
        yield rev_str[i]

input_string = "Consultadd Training"
for word in func(input_string): 
    print(word)
