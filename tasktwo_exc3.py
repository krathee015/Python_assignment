print ("Exercise 3")

a = 10
b = 20
c = 30

avg = (a + b + c)/ 3

print ("Average= ", avg)

if (avg > a and avg > b and avg > c):
    print ("Average is higher than a,b,c")

else:
    if (avg > a and avg > b):
        print ("Average is higher than a, b")
    
    elif (avg > a and avg > c):
        print ("Average is higher than a, c")
    
    elif (avg > b and avg > c):
        print ("Average is higher than b, c")
    
    else:
        if (avg > a):
            print ("Average is just higher than a")
        elif (avg > b):
            print ("Average is just higher than b")
        elif (avg > c):
            print ("Average is just higher than c")
    
            

    
        
        