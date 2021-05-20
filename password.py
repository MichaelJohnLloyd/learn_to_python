
user1 = input("Choose a Username: ")

password1 = input("Enter a password: ")


info = ["Peter", "Percy", "Paul", "Pepper", "Percival"]

def pass_unlock():

    user2 = input("What is your username? :")

    password2 = input("What is your pasword? :")

    if user1 + password1 == user2 + password2:

        print(info[4])

    else:

        print("Wrong")

pass_unlock()
