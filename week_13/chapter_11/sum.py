def main():
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  print("the summation is -> : " + str(sum(numbers, 0, 4)))

def sum(num_list, start, end):
  if start > end:
    return 0;
  else:
    return num_list[start] + sum(num_list, start + 1, end)


main()
