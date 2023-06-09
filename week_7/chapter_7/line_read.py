def main():
    infile = open('philosophers.txt', 'r')

    line_1 = infile.readline()
    line_2 = infile.readline()
    line_3 = infile.readline()

    infile.close()

    print(line_1.rstrip('\n'),line_2.strip(),line_3)

main()
