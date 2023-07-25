import random

class Coin:
    def __init__(self):
        self.sideup = 'Heads'

    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'

    def get_sideup(self):
        return self.sideup

    def change_sideup(self, sideup):
        self.sideup = sideup


def main():
    myCoin = Coin()
    pastorsCoin = Coin()
    pastorsCoin.change_sideup('horse')
    print('my coin side up: ', myCoin.get_sideup())
    print('Pastors Coin side up: ', pastorsCoin.get_sideup())

main()
