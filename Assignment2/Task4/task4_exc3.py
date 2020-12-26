print("Exercise 3")
print("Create a function that takes a list and returns a new list with unique elements of the first list.")

def unique_list(list1):
    x = [ ]

    for num in list1:
        if num not in x:
            x.append(num)

    return(x)

print("New list with unique elements: ", unique_list([4,4,6,8,9,10,0,5,6,4]))