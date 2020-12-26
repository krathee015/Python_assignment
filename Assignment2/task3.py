from typing import Sequence


print ("Exercise 1")
print ("Create a list of 10 elements of four different data types like int, string, complex and float")

complex_number = 5.5j
list_display = [1, 5, 4.4, complex_number, "KR", "DL", 7, 7.7, 9, "IN"]

print(list_display)

print("\n*****")
print("Exercise 2")
print ("Create a list of size 5 and execute the slicing structure ")

list= [1,5,8,9,6]
print("Slicing the list: ", list[0:3])

print("\n*****")
print("Exercise 3")
print (" Write a program to get the sum and multiply of all the items in a given list.")

print ("Sum of all the numbers in the list: ", sum(list))

result = 1
for num in list:
    result = result * num

print("Multipilication of all the numbres in the list: ", result)

print("\n*****")
print("Exercise 4")
print ("Find the largest and smallest number from a given list")

print ("Largest number in the given list is: ", max(list))
print ("Smallest number in the given list is: ", min(list))

print("\n*****")
print("Exercise 5")
print ("Create a new list which contains the specified numbers after removing the even numbers from apredefined list.")

list1 = [4,6,3,8,9,5,13,45,56,79]

for new_list in list1:
    if (new_list %2 == 0):
        list1.remove(new_list)
print ("List after removing even numbers is: ",list1)

print("\n*****")
print("Exercise 6")
print("A list of elements such that it contains the squares of the first and last 5 elements between 1 and 30(both included)")
list2 = []
for i in range(1,31):
    if (i in range(1,6) or i in range(25,31)):
        list2.append(i**2)
    
print("List: ", list2)

print("\n*****")
print("Exercise 7")
print("Write a program to replace the last element in a list with another list")

main_list = [1,2,3,4,5,6]
replace_list =[10,11,12]
main_list[-1: ] = replace_list
print("After replacing last value with the new list: ", main_list)

print("\n*****")
print("Exercise 8")
print("Create a new dictionary by concatenating the following two dictionaries:")
dict1 ={1:20, 2:20}
dict2 ={3:30, 4:40}
dict1.update(dict2)
print ("New dictionary after concatenation: ", dict1)

print("\n*****")
print("Exercise 9")
print("dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1 and n(both 1 and n included)")

n = eval(input("Enter the value for n: "))
dict1 = dict()
for x in range(1, n+1):
    dict1[x] = x*x
print(dict1)

print("\n*****")
print("Exercise 10")
print("a sequence of comma-separated numbers from console and generates a list and a tuple which contains every number in the form of string.")

seq1 = (input("Enter the sequence of comma-seperate numbers: "))
print ("Sequence in list: ",seq1.split(","))
print("Sequence in tuple: ", tuple(seq1.split(",")))
