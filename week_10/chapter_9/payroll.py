class Employee:
    def __init__(self, name, id, sex, position):
        self.name = name
        self.id = id
        self.sex = sex
        self.position = position

    def payroll(self, number_days, rate_day):
        print('Basic salary is: ' + str(number_days * rate_day))
    
    def print_info(self):
        print(
            'Name: ' + self.name + '\n' \
            'Id: ' + self.id + '\n' \
            'Sex: ' + self.sex + '\n'
            'Position: ' + self.position
        )

def main():
  pastor = Employee('Mr Ernest', '848204', 'M', 'Manager')
  pastor.print_info()
  pastor.payroll(20, 300)
  print('\n')
  deen = Employee('Deen', '8204', 'M', 'Janitor')
  deen.print_info()
  deen.payroll(10, 50)
main()