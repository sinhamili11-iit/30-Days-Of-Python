def scramble(word):
    scrambled_text =""
    for char in word:
        if char.lower() == "a":
            scrambled_text += "@"
        elif char.lower() == "e":
            scrambled_text += "3"
        elif char.lower() == "i":
            scrambled_text += "1"
        else:
            scrambled_text += char
    return scrambled_text
user_input = input("Enter a sentence to scramble = ")
secret_message = scramble(user_input)
print(f"Orginal sentence = {user_input}")
print(f"Scrambled sentence = {secret_message}")