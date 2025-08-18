import requests
import allure
from data import Urls


class TestGetOrder:
    @allure.title('Получаем список заказов')
    def test_get_order(self):
        order_list = requests.get(f'{Urls.scooter_url}{Urls.orders}')
        assert order_list.status_code == 200
