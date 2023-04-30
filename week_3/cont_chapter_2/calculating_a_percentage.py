original_price = int(input( \
    "Enter the original price of the product: "))

discount_amount = \
original_price * 0.2

sale_price = original_price \
  - discount_amount

print('The sale price is: ', \
       sale_price)
