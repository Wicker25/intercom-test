#!/usr/bin/env python

import click

from intercom.models import Location
from intercom.repositories import CustomerRepository
from intercom.services import get_customers_close_to_office


@click.command()
@click.option('--dataset', default='dataset/customers.txt', help='Path to the dataset.')
@click.option('--max-distance', default=100.0, type=float, help='Maximum distance from the office.')
def command(dataset, max_distance):
    office_location = Location(latitude=53.339428, longitude=-6.257664)  # Dublin
    customer_repository = CustomerRepository(dataset)

    # Get the customers close to the office and sort them by `user_id`
    customers = get_customers_close_to_office(customer_repository, office_location, max_distance)
    customers = sorted(customers, key=lambda x: x.user_id)

    for customer in customers:
        click.echo(f'[user_id={customer.user_id}] {customer.name}')


if __name__ == '__main__':
    command()

