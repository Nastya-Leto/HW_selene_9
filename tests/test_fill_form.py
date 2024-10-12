from data.test_data import path, first_name, last_name, email, phone_number, birthday, subjects, current_address, \
    download_path_picture
from pages.registration_page import RegistrationPage


def test_fill_form():
    registration_page = RegistrationPage()

    registration_page.open(path)
    registration_page.fill_first_name(first_name)
    registration_page.fill_last_name(last_name)
    registration_page.fill_user_email(email)
    registration_page.fill_female()
    registration_page.fill_user_number(phone_number)
    registration_page.fill_date_of_birth(birthday["day"], birthday["month"], birthday["year"])
    registration_page.fill_subjects(subjects)
    registration_page.fill_hobbies()
    registration_page.fill_picture(download_path_picture)
    registration_page.fill_current_address(current_address)
    registration_page.fill_state_and_city()
    registration_page.submit_button()
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
