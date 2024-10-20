import unittest
from movie import MovieCatalog, Movie  # Assuming you have this in a file named movie_catalog.py

class TestMovieCatalog(unittest.TestCase):

    def setUp(self):
        self.catalog = MovieCatalog()
        self.test_movie = self.catalog.get_movie('Challengers')


    def test_singleton(self):
        """Test that MovieCatalog is a singleton."""
        catalog1 = MovieCatalog()
        catalog2 = MovieCatalog()

        self.assertIs(catalog1, catalog2)

    def test_correct_fetching_csv(self):
        self.assertEqual(self.test_movie.title, 'Challengers')
        self.assertEqual(self.test_movie.year, 2024)
