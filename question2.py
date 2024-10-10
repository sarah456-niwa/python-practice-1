#question two.
#Using a function, create a program that calculates the volume of a cylinder 
radius=float(input("enter the value of radius :"))
height=float(input("enter the value of height :"))
import math
pie= math.pi
volume= pie*(radius**2)*height
print(f'the volume of a cylinder is {volume}')