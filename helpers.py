import fakers
import requests
from data import Urls

def generate_courier_data():
    return {
        'login': fakers.generated_login(),
        'password': fakers.generated_password(),
        'first_name': fakers.generated_firstname()
    }

def delete_courier(courier_id, courier_credentials):
    if courier_id is None:
        courier_authorization = requests.post(f'{Urls.scooter_url}{Urls.login_courier}',
                                              json={'login': courier_credentials['login'],
                                                    'password': courier_credentials['password']
                                                    }
                                              )
        courier_id = courier_authorization.json().get('id')

    response = requests.delete(f'{Urls.scooter_url}{Urls.created_courier}/{courier_id}')
    return response
