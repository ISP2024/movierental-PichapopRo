import logging
from logging import exception
from movie import Movie
from price_strategies import PriceStrategy, ChildrensPrice, NewReleasePrice, RegularPrice
import datetime


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.

    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    For simplicity of this application only days_rented is recorded.
    """

    def __init__(self, movie: Movie, days_rented, price_code: PriceStrategy):
        """Initialize a new movie rental object for
    	   a movie with known rental period (daysRented).
    	"""
        self.movie = movie
        self.days_rented = days_rented
        self.price_code = price_code

    @classmethod
    def price_code_for_movie(cls, movie: Movie) -> PriceStrategy:
        """Determines the price code for a movie."""
        current_year = datetime.date.today().year
        if movie.year == current_year:
            return NewReleasePrice()
        elif any(genre.lower() in ("Children", "Childrens") for genre in movie.genre):
            return ChildrensPrice()
        else:
            return RegularPrice()

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented

    def get_price(self):
        try:
            return self.price_code.get_price(self.days_rented)
        except exception(Exception):
            log = logging.getLogger()
            log.error(
                f"Movie {self.get_movie()} has unrecognized priceCode {self.price_code_for_movie(self.movie)}")

    def get_rental_points(self):
        """Calculates the frequent renter points for this rental."""
        return self.price_code.get_rental_points(self.days_rented)
