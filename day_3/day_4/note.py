def run_note_exercise():
    # 1. Write content with a resource guard
    notes = input("Enter your note: ")

    with open("note.txt", "w") as f:
        f.write(notes)
        
    print("Note saved successfully!")

    # 2. Defensive check when reading back
    file_name = input("Enter a file name to read: ")

    try:
        with open(file_name, "r") as f:
            print(f.read().strip())
    except FileNotFoundError:
        print(f"Diary file is currently missing: {file_name}")

    # 3. Purposely target an absent path
    try:
        with open("missing.txt", "r") as f:
            content = f.read()
    except FileNotFoundError:
        print("Safe exit: missing.txt not found")


run_note_exercise()