with open("notes.txt", "r") as original:
    content = original.read()

with open("SHOUTING.txt", "w") as new_file:
    new_file.write(content.upper())

print("File successfully converted to SHOUTING.txt!")
