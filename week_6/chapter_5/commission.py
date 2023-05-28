def main():
    keep_going = 'y'

    while keep_going == 'y':
        sales = int(input('Enter the amount of sales: '))
        comm_rate = int(input('Enter the commission rate: '))

        commission = sales * comm_rate

        print('The commission is $%.2f' %commission)

        keep_going = input('Do you want to calculate another commission (Enter y for yes): ')

        if keep_going.lower() != 'y':
            print('Its sad you have to go, see you soon')


main()
