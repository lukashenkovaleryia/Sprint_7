import pytest
from helpers import generate_courier_data


@pytest.fixture
def courier_data_auth():
    courier_data = generate_courier_data()
    courier = {
        'login': courier_data['login'],
        'password': courier_data['password']
    }
    return courier_data, courier

@pytest.fixture
def courier_data_not_login():
    courier_data = generate_courier_data()
    courier_not_login = {
        'login': '',
        'password': courier_data['password']
    }
    return courier_data, courier_not_login

@pytest.fixture
def courier_data_not_password():
    courier_data = generate_courier_data()
    courier_not_password = {
        'login': courier_data['login'],
        'password': ''
    }
    return courier_data, courier_not_password
