# values which are not divisible by 3 but are a multiple of 7. Make sure to use only higher order functions

val = filter(lambda x: x%3!=0 and x%7 ==0, range(1,101))
print(list(val))