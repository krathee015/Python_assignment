print("generate and print a tuple where the values are square of numbers between 1 and 20 (both 1 and 20 included)")

def tup_squ():

    t = list() #emply list, appending into it and converting to tuple
    for i in range(1,21):
        t.append(i**2)
    print (tuple(t))

tup_squ()