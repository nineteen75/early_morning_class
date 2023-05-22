def main():
    score = int(input('Enter your test score: \n'))

    if score < 60:
        print('Your grade is F.')
    elif score < 70: # else if score is less than 70
        print('Your grade is D')
    elif score < 80:
        print('Your grade is C')
    elif score < 90:
          print('Your grade is B')
    else:
        print('Your grade is A.')

main()