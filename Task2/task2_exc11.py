counter = 1

lucky_number = 10

while counter <= 5:
    user_number = eval(input("Guess the number: "))
    if (counter == 5):
        print ("Sorry but that was not very successful")
        break
    
    if (user_number == lucky_number):
        print ("Good guess")
        break

    elif (user_number != lucky_number):
        print ("Try again")
        counter += 1