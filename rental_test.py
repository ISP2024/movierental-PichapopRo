import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie("Dune: Part Two", Movie.NEW_RELEASE)
        self.regular_movie = Movie("Air", Movie.REGULAR)
        self.childrens_movie = Movie("Frozen", Movie.CHILDRENS)

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("Air", Movie.REGULAR)
        self.assertEqual("Air", m.get_title())
        self.assertEqual(Movie.REGULAR, m.get_price_code())

    def test_rental_price(self):
        """Test get_price method in Rental after refactoring."""
        # Test New Release movie
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(), 3.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 15.0)

        # Test for Regular movie
        rental = Rental(self.regular_movie, 1)
        self.assertEqual(rental.get_price(), 2.0)
        rental = Rental(self.regular_movie, 3)
        self.assertEqual(rental.get_price(), 3.5)

        # Test for Children's movie
        rental = Rental(self.childrens_movie, 1)
        self.assertEqual(rental.get_price(), 1.5)
        rental = Rental(self.childrens_movie, 4)
        self.assertEqual(rental.get_price(), 3.0)

    def test_rental_points(self):
        new_release_movie = Movie("New Release", Movie.NEW_RELEASE)
        regular_movie = Movie("Regular Movie", Movie.REGULAR, )
        childrens_movie = Movie("Children's Movie", Movie.CHILDRENS)
        rental = Rental(new_release_movie, 1)
        self.assertEqual(rental.rental_points(), 1)
        rental = Rental(regular_movie, 3)
        self.assertEqual(rental.rental_points(), 1)
        rental = Rental(childrens_movie, 3)
        self.assertEqual(rental.rental_points(), 1)
