import pytest
import fakers

def generate_courier():
    return {
        'login': fakers.generated_login(),
        'password': fakers.generated_password(),
        'first_name': fakers.generated_firstname()
    }

@pytest.fixture
def courier_data():
    yield generate_courier()

@pytest.fixture
def courier_data_auth():
    courier_data = generate_courier()
    courier = {
        'login': courier_data['login'],
        'password': courier_data['password']
    }
    yield courier_data, courier

@pytest.fixture
def courier_data_not_login():
    courier_data = generate_courier()
    courier_not_login = {
        'login': '',
        'password': courier_data['password']
    }
    yield courier_data, courier_not_login

@pytest.fixture
def courier_data_not_password():
    courier_data = generate_courier()
    courier_not_password = {
        'login': courier_data['login'],
        'password': ''
    }
    yield courier_data, courier_not_password
