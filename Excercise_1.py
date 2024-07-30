#Write a program that
#1) asks the user for Length and Width of a rectangle
#2) calculates and prints the area of rectangele
#3) calculates and prints the side of square that has same area


import math

Length, Width = input("Enter the Length and Width: ").split()
Area = float (Length) * float (Width)


Width = float(input("Enter Width: "))
Area = Length * Width
print("The area is :", Area)
side= math.sqrt(Area)
print ("The side of the equivalent square is: ", side)



