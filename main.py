import os

while True:
    print("\n====================")
    print(" ASSISTANT v1 ")
    print("====================")

    print("1. System Info")
    print("2. Open GitHub")
    print("0. Exit")

    choice = input("Select: ")

    if choice == "1":
        os.system("uname -a")

    elif choice == "2":
        os.system("xdg-open https://github.com")

    elif choice == "0":
        print("Goodbye")
        break

    else:
        print("Invalid option")
