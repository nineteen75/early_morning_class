def main():
 number_1 = int(input("Enter the first number: "))
 number_2 = int(input("Enter the second number: "))
 print("The GCD of the two numbers is: " + str(gcd(number_1, number_2)))

def gcd(number_1, number_2):
  if number_1 % number_2 == 0:
    return number_2
  else:
    return gcd(number_1, number_1 % number_2)

main()