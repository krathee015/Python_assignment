# filter() to make a list whose elements are even numbers between 1 and 20 (both included)

lst = filter(lambda x:x%2 == 0, range(1,21))
print(list(lst))