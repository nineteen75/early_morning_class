def show_interest(principal, rate, periods):
    interest = principal * rate * periods
    print('The simple interest will be $%.2f.' %interest)

def main():
    show_interest(rate=0.01, periods=10, principal=10000)

main()

message = 'my name is Ernest Ofosu'
def sendEmail(message):
    print("email sent")

sendEmail(message=message)