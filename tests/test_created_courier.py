import requests
import allure
from data import Urls, InvalidDataLogin, Responses
from helpers import generate_courier_data, delete_courier
import pytest


class TestCreatedCourier:

    @allure.title('Успешное создание нового курьера')
    def test_success_create_courier(self):
        courier_data = generate_courier_data()
        created_courier = requests.post(f'{Urls.scooter_url}{Urls.created_courier}',
                                        json=courier_data) # Создаём нового курьера
        assert created_courier.status_code == 201   # добавить удаление курьера?
        assert created_courier.json() == Responses.successful_created_courier
        delete_courier(courier_id=None, courier_credentials=courier_data)

    @allure.title('Попытка создать двух курьеров с одинаковыми данными')
    def test_double_create_courier(self):
        courier_data = generate_courier_data()
        created_courier = requests.post(f'{Urls.scooter_url}{Urls.created_courier}',
                                        json=courier_data)  # Создаём нового курьера
        created_courier_2 = requests.post(f'{Urls.scooter_url}{Urls.created_courier}',
                                          json=courier_data)  # Пытаемся создать курьера с такими же данными повторно
        assert created_courier.status_code == 201 # Проверяем создание нового курьера
        assert created_courier_2.status_code == 409
        delete_courier(courier_id=None, courier_credentials=courier_data)

    @allure.title('Попытка создать курьера без обязательного параметра')
    @pytest.mark.parametrize('invalid_data', [InvalidDataLogin.data, InvalidDataLogin.data_2])
    def test_create_courier_missing_required_field_shows_error(self, invalid_data):
        failed_response = requests.post(f'{Urls.scooter_url}{Urls.created_courier}', json=invalid_data)
        assert failed_response.status_code == 400
        assert failed_response.json() == Responses.invalid_login
