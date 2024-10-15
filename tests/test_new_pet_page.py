import time
import pytest
from pages.new_pet_page import NewPetPage
from pages.profile_page import ProfilePage


@pytest.mark.regression
def test_create_new_pet(browser, login):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_plus_button()
    link = 'http://34.141.58.52:8080/#/pet-new/pet'
    page = NewPetPage(browser, link)
    page.open()
    page.go_to_name()
    page.go_to_age()
    page.go_to_type()
    page.go_to_dog()
    page.go_to_gender()
    page.go_to_male()
    page.go_to_submit()
    page.go_to_add_picture()
    page.go_to_submit_add_picture()
    browser.save_screenshot('new_pet.png')


@pytest.mark.regression
def test_cancel_new_pet(browser, login):
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_plus_button()
    link = 'http://34.141.58.52:8080/#/pet-new/pet'
    page = NewPetPage(browser, link)
    page.open()
    page.go_to_name()
    page.go_to_age()
    page.go_to_type()
    page.go_to_dog()
    page.go_to_gender()
    page.go_to_male()
    page.go_to_cancel()
    browser.save_screenshot('new_pet_cancel.png')
