import requests
import allure
from data import Urls, Responses

class TestLogin:

    @allure.title('Успешная авторизация курьера')
    def test_success_authorization(self, courier_data_auth):
        courier_full_data, courier = courier_data_auth
        created_courier = requests.post(f'{Urls.scooter_url}{Urls.created_courier}', json=courier_full_data)  # Создаём нового курьера
        assert created_courier.status_code == 201 # Проверяем успешное создание курьера

        courier_authorization = requests.post(f'{Urls.scooter_url}{Urls.login_courier}', json=courier) # Авторизуемся под только что созданным курьером
        assert courier_authorization.status_code == 200

    @allure.title('Ошибка авторизации, если нет логина')
    def test_authorization_not_login(self, courier_data_not_login):
        courier_full_data, courier_not_login = courier_data_not_login
        create_courier = requests.post(f'{Urls.scooter_url}{Urls.created_courier}', json=courier_full_data)  # Создаём нового курьера
        assert create_courier.status_code == 201  # Проверяем создание курьера

        courier_authorization = requests.post(f'{Urls.scooter_url}{Urls.login_courier}', json=courier_not_login)  # Авторизуемся под только что созданным курьером без логина
        assert courier_authorization.json() == Responses.not_login
        assert courier_authorization.status_code == 400

    @allure.title('Ошибка авторизации, если нет пароля')  # Возвращает 504 статус
    def test_authorization_not_password(self, courier_data_not_password):
        courier_full_data, courier_not_password = courier_data_not_password
        create_courier = requests.post(f'{Urls.scooter_url}{Urls.created_courier}', json=courier_full_data)  # Создаём нового курьера
        assert create_courier.status_code == 201  # Проверяем создание курьера

        courier_authorization = requests.post(f'{Urls.scooter_url}{Urls.login_courier}', json=courier_not_password)  # Авторизуемся под только что созданным курьером без пароля
        assert courier_authorization.json() == Responses.not_password
        assert courier_authorization.status_code == 400

    @allure.title('Авторизация под несуществующим пользователем')  # Возвращает 504 статус
    def test_authorization_unknown_login(self):
        not_courier_data = {
            "login": 'Маша',
            "password": '1234',
            "firstName": 'Маша'
        }
        create_not_courier = requests.post(f'{Urls.scooter_url}{Urls.login_courier}', json=not_courier_data)  # Входим под несуществующим курьером
        assert create_not_courier.status_code == 404
        assert create_not_courier.json() == Responses.unknown_login


