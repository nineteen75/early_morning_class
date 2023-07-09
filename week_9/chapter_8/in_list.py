def main():
    prod_names = ['pastor', 'deen', 'ernest', 'elias']

    search = input('Enter a name to locate \n').lower()
    
    if search in prod_names:
        print(search, ' was found in the list')
    else: 
        print(search, ' was not found')

main()