import getpass
from colorama import Fore, Style, init

init(autoreset=True)

class AuthSystem:
    def __init__(self, db_manager):
        self.db = db_manager

    def display_menu(self):
        print(Fore.CYAN + "\n======================================")
        print(Fore.YELLOW + "      SHADOWS OF THE REALM - AUTH      ")
        print(Fore.CYAN + "======================================")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input(Fore.GREEN + "Select an option (1-3): " + Style.RESET_ALL).strip()
            if choice == "1":
                username = input("Username: ").strip()
                password = input("Password: ").strip()
                success, msg = self.db.authenticate_user(username, password)
                if success:
                    print(Fore.GREEN + f"\n[SUCCESS] {msg}")
                    return username
                else:
                    print(Fore.RED + f"\n[ERROR] {msg}")
            elif choice == "2":
                username = input("New Username: ").strip()
                password = input("New Password: ").strip()
                if not username or not password:
                    print(Fore.RED + "\n[ERROR] Username and password cannot be empty.")
                    continue
                success, msg = self.db.register_user(username, password)
                if success:
                    print(Fore.GREEN + f"\n[SUCCESS] {msg}")
                else:
                    print(Fore.RED + f"\n[ERROR] {msg}")
            elif choice == "3":
                print(Fore.YELLOW + "Goodbye!")
                return None
            else:
                print(Fore.RED + "Invalid option. Try again.")