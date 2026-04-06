grades = []
while True:
    entry = input("Enter any grade or type stop =")
    if entry.lower() == "stop":
        break

    num = int(entry)
    grades.append(num)
if len(grades) > 0:
    average = sum(grades)/ len(grades)
    print(f"Total grades entered : {len(grades)}")
    print(f"The average grade is {average}")
else:
    print("No grades entered.")

