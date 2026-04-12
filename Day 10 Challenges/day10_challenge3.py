accounts = {"A": 500, "B": 1000, "C": 250}

def transfer(sender, receiver, amount):
    if accounts[sender] >= amount:
        accounts[sender] -= amount
        accounts[receiver] += amount
        return "Transfer Successful!"
    else:
        return "Insufficient Funds! "

print(f"Before: {accounts}")

status = transfer("B", "A", 200)
print(status)

print(f"After: {accounts}")
