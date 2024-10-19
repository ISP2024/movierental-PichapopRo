import csv
from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class Movie:
    """A movie with title, year, and genre."""

    title: str
    year: int
    genre: set[str]

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
        """Loads movies from a CSV file."""
        with open("movies.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                title, year, genres = row
                year = int(year)
                genre_set = set(genres.split(","))
                movie = Movie(title, year, genre_set)
                self._movies[movie.title] = movie

    def get_movie(self, title: str, year: Optional[int] = None) -> Optional[Movie]:
        """Retrieves a movie by title and optional year."""
        if year:
            matching_movies = [movie for movie in self._movies.values() if movie.title == title and movie.year == year]
            if matching_movies:
                return matching_movies[0]
        else:
            return self._movies.get(title)
