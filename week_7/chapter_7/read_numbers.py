def main():
    infile = open('number.txt', 'r')

    num_1 = int(infile.readline())
    num_2 = int(infile.readline())
    num_3 = int(infile.readline())

    infile.close()

    total_numbers = num_1 + num_2 + num_3

    print('The numbers are: ', num_1, num_2, num_3)
    print('The total is: ', total_numbers)


main()