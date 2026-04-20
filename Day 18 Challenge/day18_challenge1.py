'''
TASK: Creating a string of possible characters (letters, numbers, and symbols). 
      Using a loop to pick 8 random characters from that string and join them together to create a secure password. 
'''
import random

chars = "abcdefghjkmnpqrstuvwxyz23456789!@#$%^&*"
password = ""

for i in range(8):
    password += random.choice(chars)

print(f"Your new secure password is: {password}")
