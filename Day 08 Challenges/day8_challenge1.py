age = input("Enter an age = ")
try:
    int(age)
    print (f"The entered age is {age}")
except ValueError:
    print("That's not a number! Please use digits.")