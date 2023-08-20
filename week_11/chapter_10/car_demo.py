from vehicles import Car

def main():
    used_car = Car(model='Audi', make='2007', mileage='12500', price='21500.00', doors='4')

    print('Make: ' + used_car.get_make())
    print('Model: ' + used_car.get_model())
    print('Mileage: ' + used_car.get_mileage())
    print('Price: ' + used_car.get_price())
    print('Doors: ' + used_car.get_doors())

main()