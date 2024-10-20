import re
import unittest
from price_strategies import RegularPrice, NewReleasePrice, ChildrensPrice
from customer import Customer
from rental import Rental
from movie import Movie


class CustomerTest(unittest.TestCase):
    """ Tests of the Customer class"""

    def setUp(self):
        """Test fixture contains:
        c = a customer

        movies = list of some movies
        """
        self.c = Customer("Movie Mogul")
        self.new_movie = Movie("Mulan", 2024, {"Animation", "Action"})  # Add genre
        self.regular_movie = Movie("CitizenFour", 2014, {"Documentary"})  # Add genre
        self.childrens_movie = Movie("Frozen", 2013 ,{"Animation", "Children"})  # Add genre

        self.new_release_rental = Rental(self.new_movie, 5)
        self.regular_rental = Rental(self.regular_movie, 3)
        self.childrens_rental = Rental(self.childrens_movie, 4)


    def test_statement(self):
        stmt = self.c.statement()
        # get total charges from statement using a regex
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])
        # add a rental
        self.c.add_rental(Rental(self.new_movie, 4))  # days
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace('\n', ''), flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])

    def test_total_charge(self):
        """Test the total charge calculation for all rentals."""
        self.c.add_rental(self.new_release_rental)
        self.c.add_rental(self.regular_rental)
        self.c.add_rental(self.childrens_rental)
        expected_total = (
                self.new_release_rental.get_price() +
                self.regular_rental.get_price() +
                self.childrens_rental.get_price()
        )
        self.assertEqual(self.c.total_charge(), expected_total)

    def test_total_renter_points(self):
        """Test the total frequent renter points calculation for all rentals."""
        self.c.add_rental(self.new_release_rental)
        self.c.add_rental(self.regular_rental)
        self.c.add_rental(self.childrens_rental)
        expected_points = (
            self.new_release_rental.get_rental_points() +
            self.regular_rental.get_rental_points() +
            self.childrens_rental.get_rental_points()
        )
        self.assertEqual(self.c.get_rental_points(), expected_points)
