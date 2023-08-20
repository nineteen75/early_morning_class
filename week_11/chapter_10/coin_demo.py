import simulation


def main():
    coin = simulation.Coin()
    print('This side is up: ' , coin.get_sideup())
    print('I am going to be tossing the coin ten times')

    for each_toss in range(10):
        coin.toss()
        print(coin.get_sideup())

main()