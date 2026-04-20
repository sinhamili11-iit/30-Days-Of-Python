'''
TASK: Asking the user for the radius of a circle. Using math.pi and math.pow() to calculate the Area and 
      rounding off the final answer to 2 decimal places.
'''

import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * math.pow(radius, 2)

print(f"For a radius of {radius}:")
print(f"The exact area is: {round(area, 2)}")
