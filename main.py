from database import create_user


def signup():
    username = input("Username: ")
    password = input("Password: ")

    if create_user(username, password):
        print("Account created!")
    else:
        print("Username already exists!")


def login():
    username = input("Username: ")
    password = input("Password: ")

    print(f"Logging in as {username}")


while True:
    print("\n1. Sign up")
    print("2. Login")
    print("3. Exit")

    choice = input("> ")

    if choice == "1":
        signup()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid option")