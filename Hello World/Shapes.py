# This will calculate the shapes areas.



def calculate_rectangle_area(width, height):
    area = width * height
    return area

def calculate_triangle_area(base, height):
    area = .5 * base * height
    return area

def main():
    print("This is our shapes program.")
    
    rectangle_area = calculate_rectangle_area(10,20)
    print(("The area is {}").format(rectangle_area))
    
    tri_area = calculate_triangle_area(10,20)
    print(("The area is {}").format(tri_area))


main()
