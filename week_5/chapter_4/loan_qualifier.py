def main():
    salary = input('Enter you annual salary:\n')

    years_on_job = input('Enter the number of years on current job\n')

    if float(salary) >= 30000.0:
        if int(years_on_job) >= 2:
            print ('You qualify for the loan')
        else:
            print('You mush have been on your current' +
                  'job for atleast two years to qualify')
    else:
        print('You must earn at least 30,000usd per year to qualify')

main()