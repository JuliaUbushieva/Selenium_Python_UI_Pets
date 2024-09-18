from settings import EDIT_AGE, EDIT_NAME
from .base_page import BasePage
from .locators import ProfilePageLocators


class ProfilePage(BasePage):

    def go_to_plus_button(self):
        self.browser.find_element(*ProfilePageLocators.PLUS_BUTTON).click()

    def go_to_logo(self):
        self.browser.find_element(*ProfilePageLocators.LOGO).click()

    def go_to_edit_button(self):
        self.browser.find_element(*ProfilePageLocators.EDIT_BUTTON).click()

    def go_to_delete_pet(self):
        delete_button = self.browser.find_element(*ProfilePageLocators.DELETE_BUTTON)
        delete_button.click()

    def go_to_confirm_delete_pet(self):
        confirm_delete_popup = self.browser.find_element(*ProfilePageLocators.CONFIRM_DELETE_PET)
        confirm_delete_popup.click()
        confirm_delete_pet = self.browser.find_element(*ProfilePageLocators.CONFIRM_DELETE_PET)
        confirm_delete_pet.click()

    def go_to_trash_button(self):
        self.browser.find_element(*ProfilePageLocators.TRASH_BUTTON).click()

    def go_to_edit_name(self):
        edit_name = self.browser.find_element(*ProfilePageLocators.EDIT_NAME)
        edit_name.clear()
        edit_name.send_keys(EDIT_NAME)

    def go_to_edit_age(self):
        edit_age = self.browser.find_element(*ProfilePageLocators.EDIT_AGE)
        edit_age.clear()
        edit_age.send_keys(EDIT_AGE)

    def go_to_save_edit_pet(self):
        self.browser.find_element(*ProfilePageLocators.SAVE_EDIT_PET).click()

    def go_to_edit_type(self):
        self.browser.find_element(*ProfilePageLocators.EDIT_TYPE).click()

    def go_to_reptile(self):
        self.browser.find_element(*ProfilePageLocators.REPTILE).click()

    def go_to_edit_gender(self):
        self.browser.find_element(*ProfilePageLocators.EDIT_GENDER).click()

    def go_to_female(self):
        self.browser.find_element(*ProfilePageLocators.FEMALE).click()
