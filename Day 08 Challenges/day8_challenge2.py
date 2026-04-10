def class_percentage (grade):
    if grade >=70:
        recommendation_letter = input ("Do you have a recommendation letter ?(Yes or No) = ").lower()
        if recommendation_letter == "yes":
            print("Admitted to Honours")
        else:
            print("Admitted to Standard")
    else:
        print("Application rejected")
try:
    number = int(input("Enter your grade = "))
    class_percentage(number)
except:
    print("Enter a valid number using digits!")

