#A5P2

#calculate area of polygon using math funcitons
import math
#define funcitons including main

def apothem(side_length, number_of_sides): #apothem: line from center of a polygon to one of its sides
    result = side_length / \
              (2 * math.tan(math.radians(180 / number_of_sides)))#apothem formula
    return result

def area(side_length, number_of_sides):
    perimeter = number_of_sides * side_length
    result = 0.5 * perimeter * apothem(side_length, number_of_sides)#calls apothem in area formula
    return result

def main():
    number_of_sides = int(input("Enter the number of sides: ")) #3
    side_length = float(input("Enter the side's length: ")) #5
    
    result_of_area = area(side_length, number_of_sides)
    print(f'{result_of_area:.2f}')

#call main
main()
