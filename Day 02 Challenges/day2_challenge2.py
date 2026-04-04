char_count ={}
word = input("Enter any word= ")
for char in word:
    if char in char_count:
        char_count[char] = char_count[char] + 1
    else:
        char_count[char] = 1
print(char_count)