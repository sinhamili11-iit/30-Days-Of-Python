def build_set(n, current_set):
    if n ==0:
        return current_set
    current_set.add(n)
    return build_set(n-1, current_set)
    
my_set = set()
num = int(input("Enter any number = "))
final_result = build_set(num, my_set)
print(f"The current set is{final_result}")