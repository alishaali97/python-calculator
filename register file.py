users = {}
def signup():
    print("\n=== Signup ===")
    username = input("Enter username: ")
    if username in users:
        print("Username taken! Try another.")
        return
    
    password = input("Enter password: ")
    users[username] = password
    print("Signup successful! You’re ready to go!")
def login():
    print("\n=== Login ===")
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username in users and users[username] == password:
        print("Login successful! Welcome back!")
    else:
        print("Wrong username or password. Try again!")
def main():
    while True:
        print("\n=== Login/Signup ===")
        print("1. Signup")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Pick 1, 2, or 3: ")
        
        if choice == "1":
            signup()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Bye! Come back soon!")
            break
        else:
            print("Pick 1, 2, or 3 only!")

main()
