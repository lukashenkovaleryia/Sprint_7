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
        order_id = response_order.json().get('track')
        assert response_order.status_code == 201
        requests.put(f'{Urls.scooter_url}{Urls.orders}/cancel', json = {'track': order_id})  # отменить заказ
