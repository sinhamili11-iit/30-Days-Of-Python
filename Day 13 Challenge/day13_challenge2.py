try:
    number = int(input("Enter a number to be divided by 100 = "))
    result = 100 / number
    print(f"Result : {result}")
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError :
    print("Please enter a valid number, not text")
finally:
    print("Cleanup: Connection closed and resources freed.")

