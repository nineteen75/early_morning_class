def main():
    total = 0.0

    print('This program calculates the sum of' + 
          '10 number you will enter')
    # this is called keeping a running total
    for counter in range(3):
        number = int(input("Enter a number: "))
        total += number
        # total = total + number

    print('The total is ', str(total))


main()