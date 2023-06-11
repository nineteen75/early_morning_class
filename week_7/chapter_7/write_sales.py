def main():
    number_days = int(input('For how many days to you have sales: '))

    sales_file = open('sales.txt', 'w')

    for count in range(1, number_days + 1):
        sales = input('Enter the sales for day %i: ' %count)

        sales_file.write(str(sales) + '\n')

    sales_file.close()
    print('Data written to sales.txt')

main()

#EOF - end of file

