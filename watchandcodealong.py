import math

#square 

#Ask for the information
side = float( input("what the length of a side of the square?"))

#Calculate the area
square_area = side ** 2

#Display the value
print(f"the area of the square is {square_area:.4f}cm^2")
area_in_meters = square_area / 10000
print(f"the area of the square is {area_in_meters:.4f}m^2")

#rectangle
length = float( input("what the length of the rectangle?"))
width = float( input("what the width of the rectangle?"))

rectangle_area = length * width
rectangle_area_meters = rectangle_area / 10000
print(f"the area of the rectangle is {rectangle_area}")

#circle
radus = float( input("what the radius of the circle?"))

circle_area = math.pi * radus **2
circle_area_meters = circle_area / 10000
print(f"the area of the circle is {circle_area}cm^2 or 5{circle_area_meters}m^2")

### the following works with square

#square
#Ask for the information
side = float( input("what the length of a side of the square?"))

#Calculate the area
square_area = side ** 2
print(f"the area of the square is{square_area:.4f}")