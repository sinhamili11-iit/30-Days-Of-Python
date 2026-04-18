users = {"admin" : "1234", "A" : "pass20", "guest": "00000"}
while True:
    user_name = input("Enter a user name = ").strip()
    password = input ("Enter password = ").strip()


    if user_name not in users:
        print("User does not exist")
    elif password != users[user_name]:
        print("Wrong password")
    else:
        print ("Login successful")
        break


    