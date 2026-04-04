employee= {
    101 : {"Name": "A", "Department": "HR"},
    102 : {"Name": "B", "Department" : "Writing"},
    103 : {"Name": "C", "Department" : "Management"}
}
emp_id = int(input("Enter Employee ID: "))

if emp_id in employee:
    info = employee[emp_id]
    print(f"Name: {info['Name']}, Dept: {info['Department']}")
else:
    print("Employee not found")
