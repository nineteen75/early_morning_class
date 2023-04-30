amount_due = 5000.0
monthly_payment = amount_due / 12.0

print('The monthly payment is', monthly_payment)

# with string formatting
print('The monthly payment is %.2f' % monthly_payment)

print('the numbers are: %.2f %.3f %.1f' % (3.44444, 5.333333, 6.333333))

# formatting strings
name = 'Ernest' 
last_name = 'Ofosu'
print('My name is %s' % name)
print ('Full name is: %s %s' % (name, last_name))