from collections.abc import Collection

from price_strategies import PriceStrategy
from dataclasses import dataclass


@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """
    title: str
    year: int
    genre: Collection[str]

    def is_genre(self, genre: str) -> bool:
        """Checks if the movie belongs to the given genre."""
        return genre.lower() in self.genre

    def __str__(self) -> str:
        """Returns the movie title and year in a formatted string."""
        return f"{self.title} ({self.year})"
