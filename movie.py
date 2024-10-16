from price_strategies import PriceStrategy


class Movie:
    """
    A movie available for rent.
    """

    # The types of movies (price_code).

    def __init__(self, title, price_code: PriceStrategy):
        # Initialize a new movie.
        self.title = title
        self.price_code = price_code

    def get_title(self):
        return self.title

    def get_price_code(self):
        return self.price_code

    def get_price(self, days_rented):
        return self.price_code.get_price(days_rented)

    def get_rental_points(self, days_rented):
        return self.price_code.get_rental_points(days_rented)

    def __str__(self):
        return self.title
