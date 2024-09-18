from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    FILTER_BY_TYPE = (By.XPATH, '//*[@id="typesSelector"]')
    FILTER_CAT = (By.ID, "pv_id_2_1")
    FILTER_BY_NAME = (By.XPATH, '//*[@id="petName"]')
    THUMBS_UP = (By.XPATH, "//span[@class='ml-2']")
    DETAILS_BUTTON = (By.CLASS_NAME, 'p-button-label')
    PET_PICTURE = (By.CLASS_NAME, 'p-image-preview-indicator')
    COMMENT_BLANK = (By.XPATH, '//*[@id="app"]/main/div[2]/div/div/div[3]/form/div/div/div[2]/div[1]/p')
    SAVE_COMMENT_BUTTON = (By.CLASS_NAME, 'p-button-label')


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASS = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")


class NewPetPageLocators:
    INPUT_PET_NAME = (By.ID, 'name')
    INPUT_PET_AGE = (By.CLASS_NAME, 'p-inputnumber-input')
    SELECT_PET_TYPE = (By.ID, 'typeSelector')
    SELECT_PET_GENDER = (By.ID, 'genderSelector')
    DOG = (By.XPATH, '/html/body/div[3]/div/ul/li[1]')
    MALE = (By.XPATH, '/html/body/div[3]/div/ul/li[1]')
    SUBMIT_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div/form/div/div[2]/div[3]/button[1]')
    CANCEL_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div/form/div/div[2]/div[3]/button[2]/span[2]')
    ADD_PICTURE = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div[2]/div/span/input')
    SUBMIT_ADD_PICTURE = (By. XPATH, '//*[@id="app"]/main/div/div/div[2]/div[2]/div/span')


class ProfilePageLocators:
    PLUS_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div/div[1]/div/div[1]/button/span[1]')
    LOGO = (By.CLASS_NAME, 'p-menubar-start')
    EDIT_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div[2]/div/div[2]/button[1]/span[2]')
    DELETE_BUTTON = (By.XPATH, "//span[contains(.,'Delete')]")
    CONFIRM_DELETE_POPUP = (By.CSS_SELECTOR, 'body > div.p-confirm-popup.p-component.p-ripple-disabled')
    CONFIRM_DELETE_PET = (By.XPATH, "//button[contains(.,'Yes')]")
    TRASH_BUTTON = (By.XPATH, '/html/body/div[1]/main/div/div/div[1]/div/div[2]/button')
    EDIT_NAME = (By.ID, 'name')
    EDIT_AGE = (By.XPATH, '//*[@id="age"]/input')
    EDIT_TYPE = (By.ID, 'typeSelector')
    REPTILE = (By.XPATH, '//*[@id="pv_id_8_2"]')
    EDIT_GENDER = (By.ID, 'genderSelector')
    FEMALE = (By.XPATH, '//*[@id="pv_id_9_1"]')
    SAVE_EDIT_PET = (By.XPATH, '//*[@id="app"]/main/div/form/div/div[2]/div[3]/button/span[2]')