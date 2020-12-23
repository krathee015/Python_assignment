print ("users to “guess the lucky number”. If the correct number is guessed the program stops, otherwise it continues forever.")

lucky_number =  10

while True:
    user_number = eval(input("Guess the lucky number: "))

    if (user_number == lucky_number):
        break

print("\n Modify the program")

lucky_number =  10

while True:
    user_number = eval(input("Guess the lucky number: "))
    if (user_number != lucky_number):
        answer = input("Enter if you want to continue Yes/No: ")

    if (user_number == lucky_number or answer.lower() == "no"):
        break
