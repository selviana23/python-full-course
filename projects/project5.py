movies = []


def add_movie():
    movie = input("Enter movie name: ")
    
    movie_info = {
        "title": movie,
        "watched": False
    }
    
    movies.append(movie_info)


def view_movies():
    if len(movies) == 0:
        print("No movies in your watchlist.")
    else:
        for i, movie in enumerate(movies, start=1):
            status = "Watched" if movie["watched"] else "Not Watched"
            print(i, movie["title"], "-", status)


def mark_watched():
    view_movies()

    if len(movies) > 0:
        number = int(input("Which movie did you watch? "))
        number = number - 1

        movies[number]["watched"] = True


def remove_movie():
    view_movies()

    if len(movies) > 0:
        number = int(input("Which movie do you want to remove? "))
        number = number - 1

        movies.pop(number)


while True:
    print("\n--- MOVIE WATCHLIST ---")
    print("1. Add movie")
    print("2. View movies")
    print("3. Mark as watched")
    print("4. Remove movie")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_movie()

    elif choice == "2":
        view_movies()

    elif choice == "3":
        mark_watched()

    elif choice == "4":
        remove_movie()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")