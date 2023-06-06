def sum(age_1, age_2):
    return age_1 + age_2

def main():
    first_age = int(input('enter your age: '))
    second_age = int(input('enter your best friends age: '))

    total_ages = sum(first_age, second_age)

    print('Together youa are %i' %total_ages)


main()

