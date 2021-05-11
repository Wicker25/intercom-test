import pytest

from intercom.models import Location
from intercom.repositories import CustomerRepository


@pytest.fixture()
def customer_file(tmp_path):
    file = tmp_path / 'customers.txt'
    file.write_text("""
{"latitude": "53.2451022", "user_id": 1, "name": "Ian", "longitude": "-6.238335"}
{"latitude": "54.0894797", "user_id": 2, "name": "Eoin", "longitude": "-6.18671"}
{"latitude": "52.833502", "user_id": 3, "name": "David", "longitude": "-8.522366"}
""".strip())

    return file


@pytest.fixture()
def customer_broken_file(tmp_path):
    file = tmp_path / 'customers.txt'
    file.write_text("""
{"latitude": "53.2451022", "user_id": 1, "name": "Ian", "longitude": "-6.238335"}
{"latitude": "54.0894797", "user_id": 2, BROKEN
{"latitude": "52.833502", "user_id": 3, "name": "David", "longitude": "-8.522366"}
""".strip())

    return file


def test_customer_repository_fetch_all(customer_file):
    customer_repository = CustomerRepository(customer_file)
    customers = customer_repository.fetch_all()

    assert len(customers) == 3

    assert customers[0].user_id == 1
    assert customers[0].name == 'Ian'
    assert customers[0].location == Location(latitude=53.2451022, longitude=-6.238335)

    assert customers[1].user_id == 2
    assert customers[1].name == 'Eoin'
    assert customers[1].location == Location(latitude=54.0894797, longitude=-6.18671)

    assert customers[2].user_id == 3
    assert customers[2].name == 'David'
    assert customers[2].location == Location(latitude=52.833502, longitude=-8.522366)


def test_customer_repository_invalid_filepath():
    with pytest.raises(RuntimeError, match='Invalid filepath "invalid-path.txt"'):
        CustomerRepository('invalid-path.txt')


def test_customer_repository_invalid_json(customer_broken_file):
    with pytest.raises(RuntimeError, match='Invalid JSON at line 1:.*'):
        customer_repository = CustomerRepository(customer_broken_file)
        customer_repository.fetch_all()
