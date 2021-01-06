print("Exercise 2")
# Write a program in Python to allow the user to open a file by using the argv module. If the
# entered name is incorrect throw an exception and ask them to enter the name again. Make sure
# to use read only mode.
import sys
try:
    with open(sys.argv[1],"r") as f:
        print(f.read())

except:
    print("Wrong file name entered. Please enter again")