print("generate and print a tuple where the values are square of numbers between 1 and 20 (both 1 and 20 included)")

lst = map(lambda x: x**2, range(1,21))
print(tuple(lst))