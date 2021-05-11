import pytest

from intercom.models import Location, Customer


def test_location_constructor():
    location = Location(latitude=53.339428, longitude=-6.257664)  # Dublin

    assert location.latitude == 53.339428
    assert location.longitude == -6.257664


def test_location_get_distance():
    location1 = Location(latitude=40.6892, longitude=-74.0445)  # Statue of Liberty
    location2 = Location(latitude=41.8902, longitude=12.4922)  # Colosseum

    assert location1.distance(location2) == pytest.approx(6912.153, 0.01)


def test_customer_constructor():
    location = Location(latitude=53.2451022, longitude=-6.238335)
    customer = Customer(user_id=1, name='Ian', location=location)

    assert customer.user_id == 1
    assert customer.name == 'Ian'
    assert customer.location == location


def test_customer_hash():
    location = Location(latitude=53.2451022, longitude=-6.238335)
    customer = Customer(user_id=1, name='Ian', location=location)

    assert hash(customer) == hash(Customer(user_id=1, name='Ian', location=location))
    assert hash(customer) == hash(Customer(user_id=1, name='John', location=location))
    assert hash(customer) != hash(Customer(user_id=2, name='John', location=location))


def test_customer_equality():
    location = Location(latitude=53.2451022, longitude=-6.238335)
    customer = Customer(user_id=1, name='Ian', location=location)

    assert customer == Customer(user_id=1, name='Ian', location=location)
    assert customer == Customer(user_id=1, name='John', location=location)
    assert customer != Customer(user_id=2, name='John', location=location)
