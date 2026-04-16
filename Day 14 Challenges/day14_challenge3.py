items = ["apple", "banana", "apple", "orange", "banana", "apple"]
counts = {}
for fruit in items:
    if fruit in counts:
        counts[fruit] += 1
    else:
        counts[fruit] = 1 
print(f"Frequency Count: {counts}")
