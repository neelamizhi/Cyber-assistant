import os

from modules.ui import banner
from modules.notes import save_note, view_notes
from modules.network import my_ip
from modules.password import generate_password

while True:
    os.system("clear")

    banner()

    print("1. System Info")
    print("2. My IP")
    print("3. Save Note")
    print("4. View Notes")
    print("5. Password Generator")
    print("0. Exit")

    choice = input("\nSelect: ")

    if choice == "1":
        os.system("uname -a")
        input("\nEnter to continue")

    elif choice == "2":
        my_ip()
        input("\nEnter to continue")

    elif choice == "3":
        save_note()
        input("\nEnter to continue")

    elif choice == "4":
        view_notes()
        input("\nEnter to continue")

    elif choice == "5":
        generate_password()
        input("\nEnter to continue")

    elif choice == "0":
        break

    else:
        print("Invalid")
