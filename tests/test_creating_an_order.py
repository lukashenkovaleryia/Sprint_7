import requests
import allure
from data import Urls, CreatingOrder
import pytest


class TestCreatingOrder:

    @allure.title('Создаем заказ самоката со всеми вариантами цвета самоката')
    @pytest.mark.parametrize('color', CreatingOrder.colors)
    def test_make_order_various_colors(self, color):
        data_order = CreatingOrder.order
        response_order = requests.post(f'{Urls.scooter_url}{Urls.orders}', json=data_order)
        assert response_order.status_code == 201
