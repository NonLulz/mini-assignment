
DATA_DIR = "data"
MOVIES_FILE = f"{DATA_DIR}/movies.json"
USERS_FILE = f"{DATA_DIR}/users.json"

MENU_BOOK = "1"
MENU_CANCEL = "2"



class Movie:
    def __init__(self, title, genre, total_seats):
        self.title = title
        self.genre = genre
        self.total_seats = total_seats
        self.available_seats = total_seats

    def book_seats(self, count):
        if count <= self.available_seats:
            self.available_seats -= count
            return True
        return False

    def cancel_seats(self, count):
        if self.available_seats + count <= self.total_seats:
            self.available_seats += count
            return True
        return False


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bookings = {}  # {movie_title: seat_count}


class BookingSystem:
    def __init__(self):
        self.users = {}
        self.movies = []

    def register_user(self, username, password):
        if username in self.users:
            return None
        self.users[username] = User(username, password)
        return self.users[username]

    def login(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            return user
        return None

    def add_movie(self, title, genre, seats):
        movie = Movie(title, genre, seats)
        self.movies.append(movie)
        return movie

    def find_movie(self, title):
        for movie in self.movies:
            if movie.title == title:
                return movie
        return None

    def book_seats(self, username, movie_title, count):
        user = self.users.get(username)
        movie = self.find_movie(movie_title)
        if user and movie and movie.book_seats(count):
            user.bookings[movie_title] = user.bookings.get(movie_title, 0) + count
            return True
        return False

    def cancel_booking(self, username, movie_title, count):
        user = self.users.get(username)
        movie = self.find_movie(movie_title)
        if not user or not movie:
            return False
        if movie_title not in user.bookings or user.bookings[movie_title] < count:
            return False
        if movie.cancel_seats(count):
            user.bookings[movie_title] -= count
            if user.bookings[movie_title] == 0:
                del user.bookings[movie_title]
            return True
        return False
