import json

from .models import Location, Customer


class CustomerRepository:
    """The repository used to access the customer models stored in the filesystem.
    """
    def __init__(self, filepath):
        self._filepath = filepath

    def fetch_all(self):
        output = []

        with open(self._filepath) as file:
            for line in file:
                row = json.loads(line)
                output.append(
                    self._build_customer(row, self._build_location(row))
                )

        return output

    def _build_location(self, row):
        return Location(
            latitude=float(row['latitude']),
            longitude=float(row['longitude']),
        )

    def _build_customer(self, row, location):
        return Customer(
            user_id=row['user_id'],
            name=row['name'],
            location=location,
        )
