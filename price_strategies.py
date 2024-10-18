from abc import ABC, abstractmethod


class PriceStrategy(ABC):
    """Abstract base class for rental pricing."""
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(PriceStrategy, cls).__new__(cls)
        return cls._instance

    @abstractmethod
    def get_price(self, days_rented: int) -> float:
        pass

    @abstractmethod
    def get_rental_points(self, days_rented: int) -> int:
        pass


class RegularPrice(PriceStrategy):
    """Pricing rules for regular movies."""

    def get_price(self, days_rented):
        price = 2.0
        if days_rented > 2:
            price += (days_rented - 2) * 1.5
        return price

    def get_rental_points(self, days_rented):
        return 1


class ChildrensPrice(PriceStrategy):
    """Pricing rules for children's movies."""

    def get_price(self, days_rented):
        price = 1.5
        if days_rented > 3:
            price += (days_rented - 3) * 1.5
        return price

    def get_rental_points(self, days_rented):
        return 1


class NewReleasePrice(PriceStrategy):
    """Pricing rules for new release movies."""

    def get_price(self, days_rented):
        return days_rented * 3

    def get_rental_points(self, days_rented):
        return days_rented
