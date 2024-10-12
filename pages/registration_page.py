from selene import browser, be, have

from data.test_data import file_name_download
from data.users import User


class RegistrationPage:
    def __init__(self):
        self.fill_first_name = browser.element('#firstName').should(be.blank)
        self.fill_last_name = browser.element('#lastName').should(be.blank)
        self.fill_user_email = browser.element('#userEmail').should(be.blank)
        self.fill_female = browser.element('[value=Female]')
        self.fill_user_number = browser.element('#userNumber').should(be.blank)
        self.fill_subjects = browser.element('#subjectsInput')
        self.fill_hobbies = browser.element('label[for="hobbies-checkbox-3"]')
        self.fill_picture = browser.element('#uploadPicture')
        self.fill_current_address = browser.element("[placeholder='Current Address']")
        self.fill_state = browser.element('#state').click().element('#react-select-3-option-2')
        self.fill_city = browser.element('#city').click().element('#react-select-4-option-0')
        self.submit_button = browser.element('#submit')

    def open_page(self, value):
        browser.open(value)
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def fill_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').element(f'[value = "{month}"]').click()
        browser.element('.react-datepicker__year-select').element(f'[value = "{year}"]').click()
        browser.element('.react-datepicker__month').element(f'.react-datepicker__day--0{day}').click()

    def register(self, user: User):
        self.fill_first_name.type(user.first_name)
        self.fill_last_name.type(user.last_name)
        self.fill_user_email.type(user.email)
        self.fill_female.double_click()
        self.fill_user_number.type(user.phone_number)
        self.fill_date_of_birth(user.birthday['day'], user.birthday['month'], user.birthday['year'])
        self.fill_subjects.type(user.subjects).press_tab()
        self.fill_hobbies.click()
        self.fill_picture.send_keys(file_name_download)
        self.fill_current_address.type(user.current_address)
        self.fill_state.click()
        self.fill_city.click()
        self.submit_button().click()

    def should_registered_user_with(self, full_name, email, female, number, birthday, subjects, hobbies,
                                    file_name_download,
                                    address, state):
        browser.element('.modal-content').element('table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                female,
                number,
                birthday,
                subjects,
                hobbies,
                file_name_download,
                address,
                state))
