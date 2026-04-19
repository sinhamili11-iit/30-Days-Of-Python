with open("data.txt", "w") as file:
    file.write("I love Python\nJava is okay\nPython is powerful\nCoding is fun")

with open("data.txt", "r") as file:
    for line in file:
        if "Python" in line:
            print(f"Found match: {line.strip()}")
