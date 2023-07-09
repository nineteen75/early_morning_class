def main():
    sentence = input('Enter a name: \n')
    char = input('Enter the char you want a count for: \n')
    count = 0
    for each_char in sentence:
        if each_char == char:
            count += 1
    print('"%s" has a total of %i %s characters' % (sentence, count, char))

main()
