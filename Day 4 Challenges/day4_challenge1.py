user_name= "abc11"
password = "abc@12345"
input_user_name=(input("Enter your User Name = "))
if input_user_name == user_name:
    input_password =(input("Enter your Password = "))
    if input_password == password:
        print ("Access Granted")
    else :
        print ("Invalid Password")
else:
    print ("User not Found")

