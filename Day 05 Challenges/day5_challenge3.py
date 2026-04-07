word= input("Enter any word = ")
word= word.lower()
palindrome = word[:: -1]
if word==palindrome:
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")