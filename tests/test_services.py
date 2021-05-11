import pytest

from intercom.models import Location, Customer
from intercom.services import get_customers_close_to_office


@pytest.fixture()
def customer_repository():
    class CustomerRepositoryMock:
        def fetch_all(self):
            return [
                Customer(user_id=1, name='Ian', location=Location(latitude=53.2451022, longitude=-6.238335)),
                Customer(user_id=2, name='Eoin', location=Location(latitude=54.0894797, longitude=-6.18671)),
                Customer(user_id=3, name='David', location=Location(latitude=52.833502, longitude=-8.522366)),
            ]

    return CustomerRepositoryMock()


def test_get_customers_close_to_office(customer_repository):
    office_location = Location(latitude=53.339428, longitude=-6.257664)  # Dublin

    close_customers = get_customers_close_to_office(customer_repository, office_location, 100.0)
    assert [customer.user_id for customer in close_customers] == [1, 2]
