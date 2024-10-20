import unittest
from price_strategies import RegularPrice, ChildrensPrice, NewReleasePrice
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):

    def setUp(self):

        self.new_movie = Movie("Dune: Part Two", 2023, {"Action"})
        self.regular_movie = Movie("Air", 2023, {"Drama"})
        self.childrens_movie = Movie("Frozen", 2013, {"Animation", "Children"})

    def test_rental_price(self):
        """Test get_price method in Rental after refactoring."""
        # Test New Release movie
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_price(), 2.0)
        rental = Rental(self.new_movie, 5)
        self.assertEqual(rental.get_price(), 6.5)

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
        rental = Rental(self.new_movie, 1)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.new_movie, 3)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.regular_movie, 3)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.childrens_movie, 3)
        self.assertEqual(rental.get_rental_points(), 1)