"""
WAP to calculate
Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
by importing math module
"""
import math


num = float(input("Enter a number : ")) #take input from the user

#calculate using math module 
square_root = math.sqrt(num)
N_logarithm = math.log10(num)
sin_value = math.sin(num)

#show result
print(f"square root : {square_root}")
print(f"logaritm : {N_logarithm}")
print(f"sine : {sin_value}")
