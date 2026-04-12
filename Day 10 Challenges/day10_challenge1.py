vowels = "aeiouAEIOU"
def remove_vowels(word):
    result = ""
    for char in word:
        if char not in vowels:
            result += char
    return result
string = input("Enter any string = ")
final_result = remove_vowels(string)
print(f"The string without vowels is {final_result}")

