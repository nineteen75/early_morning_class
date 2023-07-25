class Car:
    def __init__(self, name):
        self.name = name

    def stop(self):
        print("%s has stopped" % self.name)

    def start(self):
        print("%s car has started" % self.name)

    def accelerate(self):
        print("%s car is accelerating" % self.name)

def main():
    toyota = Car('toyota')
    toyota.start()
    toyota.accelerate()
    toyota.stop()
    print('\n')
    benz = Car('Benz')
    benz.start()
    benz.accelerate()
    benz.stop()

    print('\n')
    bmw = Car('bmw')
    bmw.start()
    bmw.accelerate()
    bmw.stop()

main()