def is_divisible_by_three(num):
    return num % 3 == 0
filtered_list = []
for i in range(1, 31):
    if is_divisible_by_three(i):
        filtered_list.append(i)
print(filtered_list)