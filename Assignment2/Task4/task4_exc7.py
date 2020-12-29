print("two strings as input and print the string with the maximum length in the console")

def max_length(a,b):
    len1 = len(a)
    len2 = len(b)
    if len1 > len2:
        return a
    elif len2 > len1:
        return b
    else:
        return a, b

str1 = input("enter first string: ")
str2 =input("enter second string: ")
print(max_length(str1,str2))
