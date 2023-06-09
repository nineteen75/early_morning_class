def main():
    print("Enter the names of three friends \n")
    name_1 = input('Friend #1: ')
    name_2 = input('Friend #2: ')
    name_3 = input('Friend #3: ')

    myfile = open('friends.txt', 'w')

    myfile.write(name_1 + '\n')
    myfile.write(name_2 + '\n')
    myfile.write(name_3 + '\n')

    myfile.close()

    print('The names were written to friends.txt')


main()
