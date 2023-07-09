def get_total(a_list):
    total = 0
    for value in a_list:
        total += value

    return total

def main():
    numbers = [1, 3, 6, 8, 10]
    print("The total is ", get_total(numbers))


main()