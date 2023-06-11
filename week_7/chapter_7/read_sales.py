def main():
    sales_file = open('sales.txt', 'r')

    line = sales_file.readline()

    while line != '':
        amount = float(line)

        print('$%.2f' %amount)

        line = sales_file.readline()


    sales_file.close()

main()