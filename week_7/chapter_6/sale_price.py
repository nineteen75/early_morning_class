DISCOUNT_PERCENTAGE = 0.20

def get_regular_price():
    price = int(input('Enter the items regular price: '))
    return price

def discount(price):
    return price * DISCOUNT_PERCENTAGE

def main():
    reg_price = get_regular_price()

    sale_price = reg_price - discount(reg_price)

    print('The sale price is $%.2f.' %sale_price)

main()