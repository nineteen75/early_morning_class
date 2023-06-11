def main():
    sales_file = open('sales.txt', 'r')

    for line in sales_file :
        amount = float(line)

        print('$%.2f' %amount)


    sales_file.close()

main()