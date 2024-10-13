from selene import browser, be, have

from data.users import User


class RegistrationPage:
    file_path = r"C:\Users\user\PycharmProjects\HW_selene_9\resources\image.jpg"

    def open(self, value):
        browser.open(value)
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def register(self, user: User):
        browser.element('#firstName').should(be.blank).type(user.first_name)
        browser.element('#lastName').should(be.blank).type(user.last_name)
        browser.element('#userEmail').should(be.blank).type(user.email)
        browser.element('[value=Female]').double_click()
        browser.element('#userNumber').should(be.blank).type(user.phone_number)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').element(f'[value="{user.birthday["month"]}"]').click()
        browser.element('.react-datepicker__year-select').element(f'[value="{user.birthday["year"]}"]').click()
        browser.element('.react-datepicker__month').element(f'.react-datepicker__day--0{user.birthday["day"]}').click()
        browser.element('#subjectsInput').type('Arts').press_tab()
        browser.element('label[for="hobbies-checkbox-3"]').click()
        browser.element('#uploadPicture').send_keys(RegistrationPage.file_path)
        browser.element("[placeholder='Current Address']").type(user.current_address)
        browser.element('#state').click().element('#react-select-3-option-2').click()
        browser.element('#city').click().element('#react-select-4-option-0').click()
        browser.element('#submit').click()

    def should_registered_user_with(self, user: User):
        formatted_birthday = f"{user.birthday['day']} July,{user.birthday['year']}"
        browser.element('.modal-content').element('table').all('td').even.should(
            have.exact_texts(
                user.first_name + " " + user.last_name,
                user.email,
                user.female,
                user.phone_number,
                formatted_birthday,
                user.subjects,
                user.hobbies,
                user.file_name_download,
                user.current_address,
                user.state))
