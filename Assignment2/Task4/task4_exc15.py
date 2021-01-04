# multiply the elements of a list by itself using a traditional function and pass the function to map() to complete the operation.

def multiply(x):
    return x*x

elem = map(multiply,[1,2,3,4,5,6])
print(list(elem))