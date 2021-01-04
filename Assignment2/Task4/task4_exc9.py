print("showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers")

def showNumbers(limit):

    for i in range(limit+1):
        if i%2 == 0:
            print(i, "EVEN")
        else:
            print(i, "ODD")

num = eval(input("Enter the number till you want to check: "))
showNumbers(num)

