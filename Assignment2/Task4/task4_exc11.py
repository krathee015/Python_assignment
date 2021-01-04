# map() and filter() to make a list whose elements are squares of even numbers

listUse = [1,2,3,4,5,6,7,8,9,10]

even_num = map(lambda x: x**2, filter(lambda x: x%2 == 0, listUse))

print(list(even_num))