'''
TASK: Using a for loop to count down from 3 to 1 and time.sleep(1) 
      to make the computer wait exactly 1 second, between each number.
'''

import time

print("Countdown initiated...")

for i in range(3, 0, -1):
    print(i)
    time.sleep(1) 

print("Blast off!")
