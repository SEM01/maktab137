from hw import User

def main_menu():
        print("Main Menu".center(80,"."))
        print("1) Login")
        print("2) User Managment")
        print("3) Add/Edit Travel (Just Admin)")
        print("4) Exit")

def user_manager():
    while True:
        print("User Menu".center(80,"."))
        print("1) Create Account")
        print("2) Account manager")
        print("3) Search Ticket")
        print("4) List of Users")
        print("5) Back")
        user_choise = int(input("Select option: "))
        if user_choise == 1:
            account_id = 1
            print("Create Account".center(80,"."))
            account_id = User()
            print("Confirm? ")
            user_choise = int(input("(1.yes 2.no):"))
            if user_choise == 1:
                account_id.add_user()
                account_id += 1
                print("**User Created Successfully**")
            elif user_choise == 2:
                print("**Cancel**")
        elif user_choise == 2:
            User.add_admin()
        elif user_choise == 3:
            User.search()
        elif user_choise == 4:
            User.show_user_lst()
            return
        elif user_choise == 5:
            return
while True:
    main_menu()
    user_choise = int(input("Select Option: "))
    if user_choise == 1:
        User.login()
    elif user_choise == 2:
        user_manager()
    elif user_choise == 4:
        print("Good Luck")
        break