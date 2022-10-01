class Movie:
    def __init__(self, title, genre, length, cast, director, admin_rating, show_timings, language, capacity):
        self.title = title
        self.genre = genre
        self.length = length
        self.cast = cast
        self.director = director
        self.admin_rating = admin_rating
        self.show_timings = show_timings
        self.language = language
        self.capacity = capacity


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.role = "user"
        self.booked_tickets = {}


class Users:
    users = {}

    @classmethod
    def register(self, username, user):
        self.users[username] = user

    @classmethod
    def login_user(self, username, password):
        if self.users.get(username) is None:
            return False
        if self.users.get(username).password != password:
            return False
        return True

    @classmethod
    def get_user(self, username):
        return self.users[username]


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
    ch = int(input("Enter :"))
    return ch


def admin():
    print("******Welcome Admin*******")

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



def main():
    admin = User("admin", "admin@example.com","1q2w3e4r5t6y")
    admin.role = "admin"
    Users.users[admin.email] = admin

    print("*********** WELCOME TO BOOK MY SHOW ***********")
    while True:
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        ch = int(input("Enter: "))
        if ch == 1:
            login_handler()
        elif ch== 2:
            register_handler()
        elif ch== 3:
            break
        else:
            print("Invalid input")

