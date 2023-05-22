def main():
    score = int(input('Enter your test score: \n'))

    if score < 60:
        print('Your grade is F.')
    else:
        if score < 70:
            print('Your grade is D')
        else:
            if score < 80:
                print('Your grade is C')
            else:
                if score < 90:
                    print('Your grade is B')
                else:
                    print('Your grade is A.')

main()