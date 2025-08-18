from faker import Faker

fake = Faker(locale="ru_RU")  #  генератор номеров для России

def generated_login():
    return fake.user_name()

def generated_password(length=10):
    return fake.password(length=length, special_chars=False)

def generated_firstname():
    return fake.first_name()