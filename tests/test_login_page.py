from pages.login_page import LoginPage
import allure
from allure_commons.types import AttachmentType


@allure.feature('user_login')
@allure.story('Input valid login and password')
@allure.severity('blocker')
def test_go_to_login(browser):
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_password()
    page.go_to_button()
    with allure.step('Save screenshot'):
        allure.attach(browser.get_screenshot_as_png(), name='result8', attachment_type=AttachmentType.PNG)
    browser.save_screenshot('test_login_page.png')
    profile = page.find_profile()
    assert profile

