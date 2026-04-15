data = [10, 20, 30]
index_number = int(input("Enter an index number = "))
try:
    if index_number <=3:
        print(f"The number for index {index_number} is {data[index_number]}")
except ValueError:
    print ("Please enter a valid whole number")
except IndexError:
    print("Index does not exists")