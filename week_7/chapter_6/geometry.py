from my_math import circle, rectangle

def display_menu():
    print("1) Area of a circle")
    print("2) Circumference of a circle")
    print("3) Area of a rectangle")
    print("4) Perimeter of a rectangle")
    print("5) Quit")

def main():
    display_menu()
    choice = int(input("Enter your choice"))

    if choice == 1:
        radius = int(input("Enter the circles radius: "))
        print("The area is ", circle.area(radius))

    elif choice == 2:
        radius = int(input("Enter the cicle radius: "))
        print("The circumference is: ", circle.circumference(radius))

    elif choice == 3:
        width = int(input("Enter the rectangles width: "))
        length = int(input("Enter the rectangles length: "))
        print("The area is ", rectangle.area(width, length))

    elif choice == 4:
      width = int(input("Enter the rectangles width: "))
      length = int(input("Enter the rectangles length: "))
      print("The perimeter is ", rectangle.perimeter(width, length))

    elif choice == 5:
        print("it so sad to say bye!!")

    else:
        print("Invalid selection")

main()
