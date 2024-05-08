# This will calculate the shapes areas.



def calculate_rectangle_area(width, height):
    area = width * height
    return area

def main():
    print("This is our shapes program.")
    
    rectangle_area = calculate_rectangle_area(10,20)
    print(("The area is {}").format(rectangle_area))


main()
