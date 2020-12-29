print("Exercise 1")
print ("Create a list of given structure and get the Access list")

x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]

print("Access list: ", x[5][0:4])
print("Access list: ", x[6:8])
print("Access list: ", x[0::2])
x.sort(reverse = True)
print("Access list: ", x)
print("Access list: ", x[5][5][0])
x.clear()
print("Access list: ", x)