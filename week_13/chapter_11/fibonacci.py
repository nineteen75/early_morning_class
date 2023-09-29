def main():
  number = int(input("Enter a nth number to calculate fibonacci: "))
  print("The Fibonnaci of " + str(number) + " : " + str(fibonacci(number)))


def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1 ) + fibonacci(n - 2)

main()