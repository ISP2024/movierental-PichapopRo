import csv
import logging
from dataclasses import dataclass
from typing import Optional, Collection


@dataclass(frozen=True)
class Movie:
    """A movie with title, year, and genre."""

    title: str
    year: int
    genre: Collection[str]

    def is_genre(self, genre: str) -> bool:
        """Checks if the movie belongs to the given genre."""
        return genre.lower() in self.genre

    def __str__(self) -> str:
        """Returns the movie title and year in a formatted string."""
        return f"{self.title} ({self.year})"

class MovieCatalog:
    """A singleton class for managing a collection of movies."""

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(MovieCatalog, cls).__new__(cls)
            cls._movies = {}
        return cls._instance

    def __init__(self):
        if not self._movies:
            self._load_movies()

    def _load_movies(self):
        """Loads movies from a CSV file and handles various parsing errors."""
        with open("movies.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            for row_num, row in enumerate(reader, start=1):
                if row and not row[0].startswith("#"):
                    try:
                        if len(row) < 4:
                            logging.error(f"Invalid format at row {row_num}: {row}")
                            continue
                        _, title, year_str, genres_str = row
                        try:
                            year = int(year_str)
                        except ValueError:
                            logging.error(f"Invalid year at row {row_num}: {year_str}")
                            continue
                        genre_set = list(genre.strip() for genre in genres_str.split("|"))
                        movie = Movie(title, year, genre_set)
                        self._movies[movie.title] = movie
                    except ValueError as e:
                        logging.error(f"Error parsing row {row_num}: {row}, Error: {e}")

    def get_movie(self, title: str, year: Optional[int] = None) -> Optional[Movie]:
        """Retrieves a movie by title and optional year."""
        if year:
            matching_movies = [movie for movie in self._movies.values() if movie.title == title and movie.year == year]
            if matching_movies:
                return matching_movies[0]
        else:
            return self._movies.get(title)
