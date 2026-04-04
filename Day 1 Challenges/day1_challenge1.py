import datetime
name= input("Enter your name = ")
age = int(input("Enter your age = "))
current_year= datetime.date.today().year
birth_year= current_year-age
calculated_year= birth_year +100
print(f"Hello {name}!!. You will be 100 years old in {calculated_year}")
