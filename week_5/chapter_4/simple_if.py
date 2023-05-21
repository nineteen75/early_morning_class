def authenticate_person(person):
    if person == "Pastor Ernest":
        return "welcome Pastor!"
    else:
        return "Who are you?"

def main():
    person = "Pastor Ernest"
    print(authenticate_person(person));

main()
