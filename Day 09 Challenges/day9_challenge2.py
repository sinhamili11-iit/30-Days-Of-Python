matrix = [[1, 2], [3, 4], [5, 6]]
flat_list = []
for row in matrix:
    for item in row:
        flat_list.append(item)
print(flat_list)