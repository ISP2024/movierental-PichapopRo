from price_strategies import PriceStrategy

class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code).

    def __init__(self, title, price_strategy: PriceStrategy):
        # Initialize a new movie.
        self.title = title
        self.price_strategy = price_strategy

    def get_title(self):
        return self.title

    def get_price(self, days_rented):
        return self.price_strategy.get_price(days_rented)

    def get_rental_points(self, days_rented):
        return self.price_strategy.get_rental_points(days_rented)

    def __str__(self):
        return self.title
