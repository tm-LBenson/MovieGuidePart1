def display_menu():
    """Displays the main menu."""
    print("------ Movie List Manager ------")
    print("1. Display all movies")
    print("2. Add a movie")
    print("3. Delete a movie")
    print("4. Exit")
    print("--------------------------------")

def display_movies(movie_list):
    """Displays all the movies."""
    for idx, movie in enumerate(movie_list, 1):
        print(f"{idx}. {movie}")

def add_movie(movie_list):
    """Adds a movie to the list."""
    movie_title = input("Enter the movie title to add: ")
    movie_list.append(movie_title)
    print(f"'{movie_title}' has been added!")

def delete_movie(movie_list):
    """Deletes a movie from the list."""
    try:
        display_movies(movie_list)
        movie_num = int(input("Enter the number of the movie to delete: "))
        if 1 <= movie_num <= len(movie_list):
            deleted_movie = movie_list.pop(movie_num - 1)
            print(f"'{deleted_movie}' has been deleted!")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    movie_list = ["Inception", "Interstellar", "The Matrix"]
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            display_movies(movie_list)
        elif choice == "2":
            add_movie(movie_list)
        elif choice == "3":
            delete_movie(movie_list)
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid command!")

if __name__ == "__main__":
    main()
