from functools import reduce 

print("Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce()")
lst = [1,2,3,4,5,6,7]
ls = reduce(lambda x,y: str(x)+str(y), lst)
print(ls)


