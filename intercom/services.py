"""This module contains the business logic of our application (the domain services).
"""

from .models import Location
from .repositories import CustomerRepository


def get_customers_close_to_office(
    customer_repository: CustomerRepository,
    office_location: Location,
    max_distance: float,
):
    """Returns all the customers within the given distance in km.
    """
    customers = customer_repository.fetch_all()

    return [
        customer for customer in customers
        if customer.location.distance(office_location) <= max_distance
    ]
