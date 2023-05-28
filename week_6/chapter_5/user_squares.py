def main():
    print('This program displays a list of numbers \n' +
          '(starting at 1) and their squares \n')

    end = int(input('How high should I go? '))
    print('Number\tSquare')
    print('--------------')

    for number in range(1, end+1):
        square = number**2
        print(str(number), '\t', str(square))

main()
