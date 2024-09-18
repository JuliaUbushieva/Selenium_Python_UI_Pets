from selenium_async import Keys
from settings import PET_NAME, COMMENT
from .locators import MainPageLocators
from .base_page import BasePage


class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_filter_by_type(self):
        self.browser.find_element(*MainPageLocators.FILTER_BY_TYPE).click()
        self.browser.find_element(*MainPageLocators.FILTER_CAT).click()

    def go_to_filter_by_name(self):
        filter_by_name = self.browser.find_element(*MainPageLocators.FILTER_BY_NAME)
        filter_by_name.send_keys(PET_NAME)
        filter_by_name.send_keys(Keys.ENTER)

    def thumbs_up(self):
        thumbs_up = self.browser.find_element(*MainPageLocators.THUMBS_UP)
        thumbs_up.click()

    def go_to_details_button(self):
        self.browser.find_element(*MainPageLocators.DETAILS_BUTTON).click()

    def go_to_zoom_pet_picture(self):
        self.browser.find_element(*MainPageLocators.PET_PICTURE).click()

    def go_to_comment_blank(self):
        comment_blank = self.browser.find_element(*MainPageLocators.COMMENT_BLANK)
        comment_blank.send_keys(COMMENT)
        self.browser.find_element(*MainPageLocators.SAVE_COMMENT_BUTTON).submit()
