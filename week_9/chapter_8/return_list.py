def get_values():
    values = []

    again = 'Y'

    while again.upper() == 'Y':
        num = int(input('Enter a number \n'))

        values.append(num)

        print('Do you want to add another number?')
        again = input('Y = yes, anything else = no: ')

    return values

def main():
    numbers = get_values()

    print("The numbers in the list are: ")
    print(numbers)

main()