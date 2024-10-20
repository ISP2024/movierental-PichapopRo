import unittest
from rental import Rental
from price_strategies import NewReleasePrice, ChildrensPrice, RegularPrice
from movie import Movie

class PriceCodeTest(unittest.TestCase):
    def test_new_release_price_code(self):
        movie = Movie("Top Gun: Maverick", 2024, {"Action"})
        rental = Rental(movie, 4)
        price_code = rental.price_code_for_movie(rental.movie)
        self.assertIsInstance(price_code, NewReleasePrice)

    def test_childrens_price_code(self):
        movie = Movie("Moana", 2016, {"Animation", "Children"})
        rental = Rental(movie, 4)
        price_code = rental.price_code_for_movie(rental.movie)
        self.assertIsInstance(price_code, ChildrensPrice)

    def test_regular_price_code(self):
        movie = Movie("The Godfather", 1972, {"Drama"})
        rental = Rental(movie, 4)
        price_code = rental.price_code_for_movie(rental.movie)
        self.assertIsInstance(price_code, RegularPrice)
