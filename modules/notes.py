def save_note():
    note = input("Write note: ")

    with open("data/notes.txt", "a") as file:
        file.write(note + "\n")

    print("Note saved")

def view_notes():
    try:
        with open("data/notes.txt", "r") as file:
            print(file.read())
    except:
        print("No notes found")
