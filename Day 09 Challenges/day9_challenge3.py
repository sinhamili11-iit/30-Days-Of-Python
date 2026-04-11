inventory = {"Apples" : 50, "Banana" :20, "Orange" : 10}
def check_stock (item_name):
    result = inventory.get(item_name, "Item not found")
    return result
input_item = input("Enter any item name to be checked = ")
output= check_stock(input_item)
print(f"Stock Status : {output}")