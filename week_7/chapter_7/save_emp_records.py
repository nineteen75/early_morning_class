def main():
    num_emps = int(input('How many employee records ' \
                     'do you want to create?'))

    emp_file = open('employees.txt', 'w')

    for count in range(1, num_emps + 1):
        print('Enter data for employee #%i' %count)
        name = input('Name: \n')
        id_num = input('ID: \n')
        dept = input('dept: \n')

        emp_file.write(name + '\n' + id_num + '\n' + dept + '\n')

    emp_file.close()
    print('Employee records written to employees.txt')


main()