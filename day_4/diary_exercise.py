def run_diary_exercise():
    # 1. Write content with resource guard
    with open('diary.txt', 'w') as f:
        f.write('Day 1: Started Python Learning.\n')
        f.write('Day 2: Mastered list sequences.\n')
        f.write('Day 3: Exploring safe File I/O.\n')

    # 2. Defensive check reading back
    try:
        with open('diary.txt', 'r') as f:
            print(f.read().strip())
    except FileNotFoundError:
        print("Diary file is currently missing!")

    # 3. Purposely target an absent path
    try:
        with open('missing.txt', 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print("Safe exit: missing.txt not found.")


run_diary_exercise()