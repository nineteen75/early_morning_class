def main():
    scores = [2.4, 5.2, 0.3, 4.2, 6.1]

    total = 0.0

    for value in scores:
        total += value

    average = total / len(scores)

    print("The average of the element is: ", average)

main()