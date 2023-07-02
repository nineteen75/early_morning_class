def main():
    total = 0.0

    try:
        infile = open('sales_data.txt', 'r')

        for every_line in infile:
            amount = float(every_line)
            total += amount
        
        infile.close()
        print('Total: $%.2f' % total)

    # except IOError:
    #     print('Error, file not found!')

    # except ValueError:
    #     print("Error, Non-numeric data found!")

    except:
        print('An error occured!')

main()