"""This module contains the models of our application (the domain models).
"""

from math import radians, sin, cos, acos

from dataclasses import dataclass

from .constants import EARTH_RADIUS


@dataclass(frozen=True)
class Location:
    latitude: float
    longitude: float

    def distance(self, other):
        """Returns the great-circle distance in km from another location.
        """
        latitude1, longitude1, latitude2, longitude2 = map(radians, [
            self.latitude,
            self.longitude,
            other.latitude,
            other.longitude,
        ])

        return EARTH_RADIUS * acos(
            sin(latitude1) * sin(latitude2) + cos(latitude1) * cos(latitude2) * cos(longitude1 - longitude2)
        )


class Customer:
    user_id: int
    name: str
    location: Location

    def __init__(self, *, user_id, name, location):
        self.user_id = user_id
        self.name = name
        self.location = location

    def __eq__(self, other):
        if isinstance(other, Customer):
            return self.user_id == other.user_id

        return False

    def __hash__(self):
        return hash(self.user_id)
