# Create a login page backend to ask users to enter the username and password. Make sure to
# ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
# should not be more than 3 times.

username = "testuser"
password = "test123"
counter = 1
user_name = input("Enter username: ")

while counter <= 3:   
    input_password = input("Enter password: ")
    try: 
        if user_name == username:
            if input_password != password:
                raise ValueError
            else: 
                print("All good")
                break
        else:
            print("wrong username")
            break
    except ValueError:
        counter+= 1 
        print("Incorrect password")
    
            



