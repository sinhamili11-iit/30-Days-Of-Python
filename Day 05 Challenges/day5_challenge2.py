email_address=input("Enter an email address = ")
if "@" in email_address and email_address.endswith(".com"):
    print("Valid Email")
else:
    print("Invalid Email")


