def message(times):
  if (times > 0): # base case or control
    print("This is a recursive function")
    message(times - 1) # recursive case

def main():
  message(3)

main()
