count = 0
try:
    with open("log.txt", "r") as file:
        for line in file:
            count += 1
    print(f"Total entries in log: {count}")
except FileNotFoundError:
    print("Log file not found yet!")
