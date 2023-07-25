class Employee:
    def __init__(self, name, id, sex, position):
        self.__name = name
        self.__id = id
        self.__sex = sex
        self.__position = position

    def payroll(self, number_days, rate_day):
        print('Basic salary is: ' + str(number_days * rate_day))

    def __str__(self):
        print(
            'Name: ' + self.__name + '\n' \
            'Id: ' + self.__id + '\n' \
            'Sex: ' + self.__sex + '\n'
            'Position: ' + self.__position
        )

def main():
  pastor = Employee('Mr Ernest', '848204', 'M', 'Manager')
  pastor.__str__()
  pastor.payroll(20, 300)

  print('\n')
  deen = Employee('Deen', '8204', 'M', 'Janitor')
  deen.payroll(10, 50)
  deen.__str__()
main()