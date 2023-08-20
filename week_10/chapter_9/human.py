class Human:
    '''
    for variables with preceeding double underscores means they are private
    and __variable__ is a dunder method which means it has special meaning in python
    '''
    def __init__(self, date_of_birth, time_of_birth):
        self.__date_of_birth = date_of_birth
        self.__time_of_birth = time_of_birth

    # mutator or setter
    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    def get_date_of_birth(self):
        return self.__date_of_birth

    def set_time_of_birth(self, time_of_birth):
        self.__time_of_birth = time_of_birth

    def get_time_of_birth(self):
        return self.__time_of_birth

    def __str__(self):
        return 'I was born on ' + self.__date_of_birth + ' and at ' + self.__time_of_birth

    def cry(self):
        return 'ngaaaahhhhhhhhh ngaaaaaaahhhh'

    def eating(self):
        return 'eating yum yum yum'


def main():
    baby_ernest = Human('20-12-2020', '00:20:21')
    baby_deen = Human('12-12-22', '12:23:23')
    print(baby_ernest)
    print(baby_deen)

    print('baby ernest crying ....' + baby_ernest.cry())
    print('baby deen crying ....' + baby_deen.cry())

main()

'''
classes names should start with caps
Human, House, Birds

Accessors and Mutators
or
Getters and Setters
'''
