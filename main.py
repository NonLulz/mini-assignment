# class Movie:
#     def __init__(self, title, genre, length, cast, director, admin_rating, show_timings, language, capacity):
#         self.title = title
#         self.genre = genre
#         self.length = length
#         self.cast = cast
#         self.director = director
#         self.admin_rating = admin_rating
#         self.show_timings = show_timings
#         self.language = language
#         self.capacity = capacity

import hashlib
from typing import Dict
from booking_system import BookingSystem


class Movie:
    """
    Represents a movie/show with relevant details.
    """

    def __init__(
        self,
        title: str,
        genre: str,
        length: int,  # in minutes
        cast: list[str],
        director: str,
        admin_rating: float,  # 0.0 - 10.0
        show_timings: list[str],  # e.g., ["10:00 AM", "2:00 PM"]
        language: str,
        capacity: int  # max audience capacity
    ) -> None:
        """
        Initialize a Movie object.

        Args:
            title (str): The name of the movie.
            genre (str): The genre (e.g., "Action", "Comedy").
            length (int): Duration of the movie in minutes.
            cast (list[str]): List of actors/actresses.
            director (str): Name of the director.
            admin_rating (float): Rating assigned by admin (0.0 to 10.0).
            show_timings (list[str]): Available show times.
            language (str): Language of the movie.
            capacity (int): Maximum seating capacity for the show.
        """
        if not title:
            raise ValueError("Movie title cannot be empty.")
        if length <= 0:
            raise ValueError("Movie length must be a positive number.")
        if not (0.0 <= admin_rating <= 10.0):
            raise ValueError("Admin rating must be between 0.0 and 10.0.")
        if capacity <= 0:
            raise ValueError("Capacity must be a positive number.")

        self.title = title
        self.genre = genre
        self.length = length
        self.cast = cast
        self.director = director
        self.admin_rating = admin_rating
        self.show_timings = show_timings
        self.language = language
        self.capacity = capacity

# class User:
#     def __init__(self, name, email, password):
#         self.name = name
#         self.email = email
#         self.password = password
#         self.role = "user"
#         self.booked_tickets = {}


# class Users:
#     users = {}

#     @classmethod
#     def register(self, username, user):
#         self.users[username] = user

#     @classmethod
#     def login_user(self, username, password):
#         if self.users.get(username) is None:
#             return False
#         if self.users.get(username).password != password:
#             return False
#         return True

#     @classmethod
#     def get_user(self, username):
#         return self.users[username]

class User:
    """
    Represents a single user in the system.
    """

    def __init__(self, name: str, email: str, password: str) -> None:
        """
        Initialize a User object.

        Args:
            name (str): The user's full name.
            email (str): The user's email address.
            password (str): The user's password (will be stored as a hash).
        """
        if not name:
            raise ValueError("Name cannot be empty.")
        if "@" not in email:
            raise ValueError("Invalid email address.")
        if not password or len(password) < 6:
            raise ValueError("Password must be at least 6 characters long.")

        self.name: str = name
        self.email: str = email
        self.password: str = self._hash_password(password)
        self.role: str = "user"
        self.booked_tickets: Dict[str, int] = {}  # movie_title -> tickets booked

    def _hash_password(self, password: str) -> str:
        """Hash the password using SHA-256 for security."""
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password: str) -> bool:
        """Verify a provided password against the stored hash."""
        return self.password == hashlib.sha256(password.encode()).hexdigest()


class Users:
    """
    Manages a collection of registered users.
    """
    users: Dict[str, User] = {}

    @classmethod
    def register(cls, username: str, user: User) -> None:
        """
        Register a new user.

        Args:
            username (str): Unique username identifier.
            user (User): User object.
        """
        if username in cls.users:
            raise ValueError("Username already exists.")
        cls.users[username] = user

    @classmethod
    def login_user(cls, username: str, password: str) -> bool:
        """
        Validate login credentials.

        Args:
            username (str): Username identifier.
            password (str): Plain-text password to verify.

        Returns:
            bool: True if login is successful, False otherwise.
        """
        user = cls.users.get(username)
        if user is None:
            return False
        return user.verify_password(password)

    @classmethod
    def get_user(cls, username: str) -> User | None:
        """
        Retrieve a user by username.

        Args:
            username (str): Username identifier.

        Returns:
            User | None: User object if found, otherwise None.
        """
        return cls.users.get(username)

class Movies:
    movies = {}

    @classmethod
    def add_movie(self, movie_title, movie):
        self.movies[movie_title] = movie

    @classmethod
    def update_movie(self, movie_title, movie):
        self.movies[movie_title] = movie

    @classmethod
    def delete_movie(self, movie_title):
        self.movies.pop(movie_title)


def register():
    print("**** Create new Account *****")
    name = input("Name: ")
    email = input("Email: ")
    password = input("Password: ")

    new_user = User(name, email, password)
    Users.register(email, new_user)

def login():
    email = input("Email: ")
    password = input("Password: ")

    if Users.login_user(email, password) is False:
        print("Invalid email or password !")
        return

    user = Users.get_user(email)

    if user.role == "admin":
        admin()


def movie():
    title = input("Title: ")
    genre = input("Genre: ")
    length = int(input("length: "))
    cast = input("Cast: ")
    director = input("Director: ")
    admin_rating = input("Rating: ")
    language = input("Language: ")
    show_timings = input("Show Timings: ")
    capacity = int(input("Capacity: "))

    return Movie(title, genre, length, cast, director, admin_rating, show_timings, language, capacity)

def display(movie):
    print("Title :", movie.title)
    print("Genre :", movie.genre)
    print("Length :", movie.length)
    print("Cast :", movie.cast)
    print("Director :", movie.director)
    print("Admin Rating :", movie.admin_rating, "/10")
    print("Show Timings :", movie.show_timings)
    print("1. Book Tickets")
    print("2. Cancel Tickets")
    choice = int(input("Enter :"))
    return choice


def admin():
    print("******Welcome Admin********")

    while True:
        print("1. Add New Movie")
        print("2. Edit Movie")
        print("3. Delete Movie")
        print("4. Logout")

        choice = int(input("Enter: "))

        if choice == 1:
            movie = input_movie_details()
            Movies.movies[movie.title] = movie
        elif choice == 2:
            title = input("Enter title of the movie to be updated: ")

            if Movies.movies.get(title) is None:
                print("Movie does not exist..")
                continue

            movie = input_movie_details()
            Movies.movies[title] = movie
        elif choice == 3:
            title = input("Enter title of the movie to be updated: ")

            if Movies.movies.get(title) is None:
                print("Movie does not exist..")
                continue

            Movies.movies.pop(title)
        elif choice == 4:
            return
        else:
            print("Invalid input")


def book_tickets(movie):

    if movie.capacity == 0:
        print("Housefull")
        return



# def main():
#     admin = User("admin", "admin@example.com","1q2w3e4r5t6y")
#     admin.role = "admin"
#     Users.users[admin.email] = admin

#     print("*********** WELCOME TO BOOK MY SHOW ***********")
#     while True:
#         print("1. Login")
#         print("2. Register")
#         print("3. Exit")

#         ch = int(input("Enter: "))
#         if ch == 1:
#             login_handler()
#         elif ch== 2:
#             register_handler()
#         elif ch== 3:
#             break
#         else:
#             print("Invalid input")

# def main() -> None:
#     """
#     Entry point for the Book My Show application.
#     Provides a simple CLI menu for user login, registration, and exit.
#     """

#     # Create admin user (for demo purposes only; in real apps, load from config/DB)
#     admin = User("admin", "admin@example.com", "1q2w3e4r5t6y")
#     admin.role = "admin"
#     Users.register(admin.email, admin)

#     print("\n*********** WELCOME TO BOOK MY SHOW ***********\n")

#     while True:
#         print("1. Login")
#         print("2. Register")
#         print("3. Exit")

#         choice = input("Enter choice: ").strip()

#         if not choice.isdigit():
#             print("Invalid input. Please enter a number.\n")
#             continue

#         ch = int(choice)
#         if ch == 1:
#             login_handler()
#         elif ch == 2:
#             register_handler()
#         elif ch == 3:
#             print("Exiting... Goodbye!")
#             break
#         else:
#             print("Invalid option. Please try again.\n")

# print("\033[92m✅ Booking successful!\033[0m")  # Green
# print("\033[91m❌ Booking failed: Not enough seats.\033[0m")  # Red


def prompt_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("\033[91m⚠️ Please enter a valid number.\033[0m")

def main():
    system = BookingSystem()

    while True:
        print("\nMovies Available:")
        system.list_movies()
        print("\nOptions:")
        print("1. Book seats")
        print("2. Cancel booking")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            user = system.login(username, password)
            if not user:
                print("\033[91m❌ Invalid login credentials.\033[0m")
                continue

            movie_title = input("Enter movie title: ").strip()
            count = prompt_int("Number of seats to book: ")

            if system.book_seats(username, movie_title, count):
                print("\033[92m✅ Booking successful!\033[0m")
            else:
                print("\033[91m❌ Booking failed. Not enough seats or invalid movie.\033[0m")

        elif choice == "2":
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            user = system.login(username, password)
            if not user:
                print("\033[91m❌ Invalid login credentials.\033[0m")
                continue

            movie_title = input("Enter movie title to cancel booking: ").strip()
            count = prompt_int("Number of seats to cancel: ")

            if system.cancel_booking(username, movie_title, count):
                print("\033[92m✅ Cancellation successful!\033[0m")
            else:
                print("\033[91m❌ Cancellation failed. Check your bookings.\033[0m")

        elif choice == "3":
            print("Exiting. Goodbye!")
            break
        else:
            print("\033[91m⚠️ Invalid option. Please try again.\033[0m")

if __name__ == "__main__":
    main()


