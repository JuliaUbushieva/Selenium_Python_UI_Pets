import pytest
from pages.profile_page import ProfilePage
import time


def test_delete_pet(browser, login):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_delete_pet()
    page.go_to_confirm_delete_pet()
    browser.save_screenshot('delete_pet.png')


@pytest.mark.skip
def test_trash_button(browser, login):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_trash_button()
    browser.save_screenshot('trash_btn.png')


@pytest.mark.regression
def test_edit_pet_name(browser, login):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_edit_button()
    page.go_to_edit_name()
    page.go_to_save_edit_pet()
    browser.save_screenshot('edit_pet_name.png')


@pytest.mark.regression
def test_edit_pet_age(browser, login):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_edit_button()
    page.go_to_edit_age()
    page.go_to_save_edit_pet()
    browser.save_screenshot('edit_pet_age.png')
