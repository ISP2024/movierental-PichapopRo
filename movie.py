from price_strategies import PriceStrategy


class Movie:
    """
    A movie available for rent.
    """

    # The types of movies (price_code).

    def __init__(self, title):
        # Initialize a new movie.
        self.title = title

    def get_title(self):
        return self.title

    def __str__(self):
        return self.title
