import requests
import allure
from data import Urls, Responses, not_courier_data
from helpers import delete_courier

class TestLogin:

    @allure.title('Успешная авторизация курьера')
    def test_success_authorization(self, courier_data_auth):
        courier_full_data, courier_credentials = courier_data_auth
        created_courier = requests.post(f'{Urls.scooter_url}{Urls.created_courier}', json=courier_full_data)  # Создаём нового курьера
        courier_authorization = requests.post(f'{Urls.scooter_url}{Urls.login_courier}', json=courier_credentials) # Авторизуемся под только что созданным курьером
        courier_id = courier_authorization.json().get('id')
        assert created_courier.status_code == 201         # Проверяем успешное создание курьера
        assert courier_authorization.status_code == 200   # и его успешную авторизацию
        delete_courier(courier_id, courier_credentials)

    @allure.title('Ошибка авторизации, если нет логина')
    def test_authorization_not_login(self, courier_data_not_login):
        courier_full_data, courier_not_login = courier_data_not_login
        created_courier = requests.post(f'{Urls.scooter_url}{Urls.created_courier}', json=courier_full_data)  # Создаём нового курьера
        courier_authorization = requests.post(f'{Urls.scooter_url}{Urls.login_courier}', json=courier_not_login)  # Авторизуемся под только что созданным курьером без логина
        assert created_courier.status_code == 201    # Проверяем создание курьера
        assert courier_authorization.status_code == 400 and courier_authorization.json() == Responses.not_login   # и проблемы с его авторизацией
        delete_courier(courier_id=None, courier_credentials=courier_full_data)

    @allure.title('Ошибка авторизации, если нет пароля')  # Возвращает 504 статус
    def test_authorization_not_password(self, courier_data_not_password):
        courier_full_data, courier_not_password = courier_data_not_password
        created_courier = requests.post(f'{Urls.scooter_url}{Urls.created_courier}', json=courier_full_data)  # Создаём нового курьера
        courier_authorization = requests.post(f'{Urls.scooter_url}{Urls.login_courier}', json=courier_not_password)  # Авторизуемся под только что созданным курьером без пароля
        assert created_courier.status_code == 201  # Проверяем создание курьера
        assert courier_authorization.status_code == 400 and courier_authorization.json() == Responses.not_password # и проблемы с его авторизацией
        delete_courier(courier_id=None, courier_credentials=courier_full_data)

    @allure.title('Авторизация под несуществующим пользователем')  # Возвращает 504 статус
    def test_authorization_unknown_login(self):
        create_not_courier = requests.post(f'{Urls.scooter_url}{Urls.login_courier}', json=not_courier_data)  # Входим под несуществующим курьером
        assert create_not_courier.status_code == 404
        assert create_not_courier.json() == Responses.unknown_login
