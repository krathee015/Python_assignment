print("Exercise 1")
print ("Create a list of given structure and get the Access list")

x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]

print("Access list: ", x[5][0:4])
print("Access list: ", x[6:8])
print("Access list: ", x[0::2])
print("Access list: ", x[::-1])
print("Access list: ", x[5][5][0])
x.clear()
print("Access list: ", x)

print("\n******")
print("Exercise2")
print("list of thousand numbers using range and xrange and see the difference between each other.")

range_list = range(1,1000)
# xrange_list = xrange(1,1000)
print("thousand numbers using range: ",range_list)
# print("thousand numbers using range: ",xrange_list)

print("\n******")
print("Exercise3")
print ("How Tuple is beneficial as compared to the list?")
print("Tuple is beneficial as compared to the list as it is faster due to the static nature")

print("\n******")
print("Exercise4")
print("iterate through the list of numbers in the range of 1,100 and print the number which is divisible by 3 and is a multiple of 2")

list1 = range(1,100)
for i in range(len(list1)):
    if (list1[i] %3 ==0  and list1[i]%2 ==0):
        print(list1[i])

print("\n******")
print("Exercise5")
print("reverse a string and print only the vowel alphabet if it exists in the string with their index.")
str = input("Enter a string: ")
arr = ["a","e","i","o","u"]
str_reverse = str[::-1]
print("String after reverse: ",str_reverse)
for i in range(len(str_reverse)):
    if str_reverse[i] in arr:
        index = str.index(str_reverse[i])
        print(str_reverse[i],"Vowel has index: ",index)

print("\n******")
print("Exercise6")
print ("iterate through the string “hello my name is abcde” and print the string which is having an even length.")

str = "Hello my name is Abcde"
print("The string is: ",str)
words = list(str.split(" "))
print("Even length words are: ")
for i in words:
    if(len(i) %2 == 0):
        print(i)

print("\n******")
print("Exercise7")
print("print the pair of numbers whose sum is equal to the result number that is let's say 8.")

x=[1,2,3,4,5,6,7,8,9,-1]
n = len(x)
count = 0
sum = 8
for i in range(0, n):
    for j in range(i+1, n):
        if x[i] + x[j] == sum:
            count+= 1
print("Counts of pair of number: ",count)

print("\n******")
print("Exercise8")
# Create two lists such as even_list and odd_list
even_list = []
odd_list =[]
counter = 0
while counter <10:
    num = int(input("Enter the number between 1-50: "))
    if num%2 == 0:
        if len(even_list) < 5: 
            even_list.append(num)
    else:
        if len(odd_list) < 5:
            odd_list.append(num)
    counter+= 1

print("Even list: ",even_list)
print("Odd list: ",odd_list)
sum_even = 0
for num in range(len(even_list)):
    sum_even = sum_even + even_list[num]

sum_odd = 0
for num in range(len(odd_list)):
    sum_odd = sum_odd + odd_list[num]

if sum_even > sum_odd:
    print("The maxium list is even list: ",sum_even)
else:
    print("The maxium list is odd list: ",sum_odd)

print("\n******")
print("Exercise9")
print("find out the occurrence of a specific character from an alphanumeric string")
alpha_numeric = "12abcbacbaba344ab"
count = { }

for i in range(len(alpha_numeric)):
    if alpha_numeric[i].isdigit():
        continue
    else:
        if alpha_numeric[i] in count:
            count[alpha_numeric[i]]+= 1
        else:
            count[alpha_numeric[i]] = 1
print(count)

print("\n******")
print("Exercise10")
print(" Generate and print another tuple whose values are even numbers in the given tuple")
tup = (1,2,3,4,5,6,7,8,9,10)
new_tup = ()
new_list = []
t_to_l = list(tup)
for i in range(len(t_to_l)):
    if (t_to_l[i] %2 == 0):
        new_list.append(t_to_l[i])
        new_tup = tuple(new_list)

print("Tuple after adding even numbers: ",new_tup)





