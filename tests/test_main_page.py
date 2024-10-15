import time
import pytest
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


@pytest.mark.smoke
def test_go_to_login_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    browser.save_screenshot('main_page.png')


@pytest.mark.smoke
def test_go_to_filter_by_type(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_filter_by_type()
    browser.save_screenshot('filter_by_type.png')


@pytest.mark.smoke
def test_go_to_filter_by_name(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_filter_by_name()
    browser.save_screenshot('filter_by_name.png')


@pytest.mark.xfail
def test_thumbs_up(browser, login):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_logo()
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.thumbs_up()
    browser.save_screenshot('thumbs_up.png')


@pytest.mark.skip
def test_zoom_pet_picture(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_details_button()
    page.go_to_zoom_pet_picture()
    browser.save_screenshot('pet_picture.png')


@pytest.mark.xfail
def test_comment(browser, login):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_logo()
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_details_button()
    page.go_to_comment_blank()
    browser.save_screenshot('pet_comment.png')
