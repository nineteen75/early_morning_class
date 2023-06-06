def is_even(number):
    if (number % 2) == 0:
        status = True
    else:
        status = False

    return status

def main():
    num = int(input("Enter a number: "))
    print("is %i even? " %num, is_even(num) )

main()