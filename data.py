import fakers


class Urls:
    scooter_url = 'https://qa-scooter.praktikum-services.ru'
    created_courier = '/api/v1/courier'
    login_courier = '/api/v1/courier/login'
    orders = '/api/v1/orders'


class Responses:
    successful_created_courier = {'ok': True} # Курьер успешно создан
    double_created_courier = {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'} # Попытка создания второго курьера с одинаковыми данными
    invalid_login = {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
    not_login = {'code': 400, 'message': 'Недостаточно данных для входа'}
    not_password = {'code': 400, 'message': 'Недостаточно данных для входа'}
    unknown_login = {'code': 404, 'message': 'Учетная запись не найдена'}


class InvalidDataLogin:
    data = {'password': fakers.generated_password(), 'first_name': fakers.generated_firstname()}
    data_2 = {'login': fakers.generated_login(), 'first_name': 'NNN'}


class CreatingOrder:
    order = {
        'firstName': 'Chaplin',
        'lastName': 'Chaplin',
        'address': 'lenina 55',
        'metroStation': 1,
        'phone': '+79999999999',
        'rentTime': 1,
        'deliveryDate': '2025-08-22',
        'comment': 'Ne zvonit'
    }
    colors = [
        ['BLACK'],
        ['GREY'],
        (['BLACK'], ['GREY']),
        ['']
    ]


not_courier_data = {
    "login": 'Маша',
    "password": '1234',
    "firstName": 'Маша'
}
