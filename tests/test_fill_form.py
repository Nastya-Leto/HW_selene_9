from data.test_data import path
from data.users import student
from pages.registration_page import RegistrationPage


def test_fill_form():
    registration_page = RegistrationPage()
    registration_page.open_page(path)
    registration_page.register(student)
    registration_page.should_registered_user_with(
        'Анастасия З',
        'test@mail.ru',
        'Female',
        '7927000000',
        '20 July,1995',
        'Arts',
        'Music',
        'image.jpg',
        'Samara',
        'Haryana Karnal')
