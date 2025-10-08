import unittest
from booking_system import BookingSystem, Movie, User

class TestBookingSystem(unittest.TestCase):

    def setUp(self):
        self.system = BookingSystem()
        self.user = self.system.register_user("alice", "password123")
        self.system.add_movie("Inception", "Sci-Fi", 10)

    def test_add_movie(self):
        self.assertEqual(len(self.system.movies), 1)
        self.assertEqual(self.system.movies[0].title, "Inception")

    def test_user_registration_and_login(self):
        user2 = self.system.register_user("bob", "pass")
        logged_in_user = self.system.login("bob", "pass")
        self.assertEqual(logged_in_user.username, "bob")

    def test_successful_booking(self):
        movie = self.system.movies[0]
        booking_result = self.system.book_seats("alice", movie.title, 2)
        self.assertTrue(booking_result)
        self.assertEqual(movie.available_seats, 8)

    def test_booking_more_than_available(self):
        movie = self.system.movies[0]
        booking_result = self.system.book_seats("alice", movie.title, 15)
        self.assertFalse(booking_result)

    def test_cancel_booking(self):
        movie = self.system.movies[0]
        self.system.book_seats("alice", movie.title, 3)
        cancel_result = self.system.cancel_booking("alice", movie.title, 3)
        self.assertTrue(cancel_result)
        self.assertEqual(movie.available_seats, 10)

    def test_invalid_login(self):
        self.assertIsNone(self.system.login("nonexistent", "wrongpass"))

