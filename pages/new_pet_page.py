from settings import NEW_PET_NAME, NEW_PET_AGE, NEW_PET_PICTURE
from .base_page import BasePage
from .locators import NewPetPageLocators


class NewPetPage(BasePage):

    def go_to_name(self):
        new_name = self.browser.find_element(*NewPetPageLocators.INPUT_PET_NAME)
        new_name.send_keys(NEW_PET_NAME)

    def go_to_age(self):
        new_age = self.browser.find_element(*NewPetPageLocators.INPUT_PET_AGE)
        new_age.send_keys(NEW_PET_AGE)

    def go_to_type(self):
        self.browser.find_element(*NewPetPageLocators.SELECT_PET_TYPE).click()

    def go_to_dog(self):
        self.browser.find_element(*NewPetPageLocators.DOG).click()

    def go_to_gender(self):
        self.browser.find_element(*NewPetPageLocators.SELECT_PET_GENDER).click()

    def go_to_male(self):
        self.browser.find_element(*NewPetPageLocators.MALE).click()

    def go_to_submit(self):
        self.browser.find_element(*NewPetPageLocators.SUBMIT_BUTTON).click()

    def go_to_cancel(self):
        self.browser.find_element(*NewPetPageLocators.CANCEL_BUTTON).click()

    def go_to_add_picture(self):
        add_photo = self.browser.find_element(*NewPetPageLocators.ADD_PICTURE)
        add_photo.send_keys(NEW_PET_PICTURE)

    def go_to_submit_add_picture(self):
        submit_add_picture = self.browser.find_element(*NewPetPageLocators.SUBMIT_ADD_PICTURE)
        submit_add_picture.click()
