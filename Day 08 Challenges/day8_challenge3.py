def process_data(my_list):
    unique_list = list(set(my_list))
    new_list = []
    for num in unique_list:
        if num % 2 == 0:
            new_list.append(num)
    return new_list
my_data = [1, 2, 2, 3, 4, 4, 5, 6, 6, 10]
result = process_data(my_data)
print(f"Unique Even numbers are : {result}")