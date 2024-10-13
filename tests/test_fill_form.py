from data.users import student
from pages.registration_page import RegistrationPage


def test_fill_form():
    registration_page = RegistrationPage()
    registration_page.open('/automation-practice-form')
    registration_page.register(student)
    registration_page.should_registered_user_with(student)
