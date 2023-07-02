def main():
    num = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))

    # if num2 != 0:
    #   result = num / num2
    #   print('%f divided by %f = %f' % (num, num2, result))
    # else:
    #    print('Cannot divide by zero')
    try:
        result = num / num2
        print('%f divided by %f = %f' % (num, num2, result))
    except ZeroDivisionError:
        print('You cant divide by zero, Error!')


main()