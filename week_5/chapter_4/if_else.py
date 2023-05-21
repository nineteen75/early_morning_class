def authenticate_person(person):
    if person.lower() == "Ernest".lower():
        return "welcome Pastor!"
    elif person.lower() == "Elias".lower():
        return "Welcome Elias"
    elif person.lower == "Tawiah".lower():
        return "Welcome Tawiah"
    elif person.lower == "Ofosu".lower():
        return "Welcome Ofosu"
    else:
        return "Who are you?"

def main():
    person = input("What is your name?\n")
    print(authenticate_person(person));

main()
