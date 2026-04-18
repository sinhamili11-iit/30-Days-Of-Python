messy_list = ["apple", "banana", "apple", "orange", "banana", "grape"]
clean_list = []
for item in messy_list:
    if item not in clean_list:
        clean_list.append(item)
    else:
        print(f"Skipping duplicate : {item}")
print(f"Original List : {messy_list}")
print(f"Clean_list : {clean_list}")