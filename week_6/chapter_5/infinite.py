def main():
    keep_going = 'y'

    while keep_going == 'y':
        sales = int(input('Enter the amount of sales: '))
        comm_rate = int(input('Enter the commission rate: '))

        commission = sales * comm_rate

        print('The commission is $%.2f' %commission)


main()
