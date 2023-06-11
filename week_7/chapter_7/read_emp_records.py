def main():
    emp_file = open('employees.txt', 'r')

    name = emp_file.readline()

    while name != '':
        id_num = emp_file.readline()
        dept = emp_file.readline()

        name = name.rstrip('\n')
        id_num = id_num.strip('\n')
        dept = dept.strip('\n')

        print('Name: ', name)
        print('ID: ', id_num)
        print('Dept: ', dept)

        name = emp_file.readline()

    emp_file.close()
    print('Done reading the file ..')


main()
