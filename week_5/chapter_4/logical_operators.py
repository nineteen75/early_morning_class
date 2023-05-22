def main():
    score = int(input('Enter your test score: \n'))

    if score <= 60:
        print('Your grade is F')
    elif score >= 61 and score <= 70:
        print('Your grade is D')
    elif score >= 71 and score <= 80:
        print('Your grade is C')
    elif score >= 81 and score <= 90:
        print('Your grade is B')
    else:
        print('Your grade is A')

main()