from selenium.webdriver.common.by import By
from random import randint
class FormPageLocators:
    LAST_NAME = (By.CSS_SELECTOR, '#lastName')
    FIRST_NAME = (By.CSS_SELECTOR, '#firstName')
    EMAIL = (By.CSS_SELECTOR, '#userName')
    GENDER = (By.CSS_SELECTOR, f'for="gender-radio-{randint(1,3)}"')
    MOBILE = (By.CSS_SELECTOR, '#userNumber')
    SUBJECT = (By.CSS_SELECTOR, '#subjectsInput')
    FILE_INPUT = (By.CSS_SELECTOR, '#uploadPicture')
    CALENDARY = (By.XPATH, "// input[ @ id = 'dateOfBirthInput']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, '#curentAddress')
    SUBMIT = (By.CSS_SELECTOR, '#submit')



