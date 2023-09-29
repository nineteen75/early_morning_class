def main():
  number = int(input("Enter a non-negative number: "))
  print("The Factorial of " + str(number) + " : " + str(factorial(number)))

def factorial(num):
  if num == 0:
    return 1
  else:
    return num * factorial(num - 1)

main()