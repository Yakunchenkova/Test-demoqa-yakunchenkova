from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators

class FormPage(BasePage):

    def fill_fields_and_submit(self):
        first_name ='Inna'
        last_name ='Yakunchenkova'
        email ="innayakunchenkova@gmail.com"
        self.remove_footer()
        self.element_is_visible(Locators.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(Locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.GENDER).click()
        self.element_is_visible(Locators.MOBILE).send_keys('4569781234')
        subject= self.element_is_visible(Locators.SUBJECT)
        subject.send_keys('English')
        subject.send_keys(Keys.RETURN)
        self.element_is_visible(Locators.FILE_INPUT).send_keys(r'C:\Users\yakun\PycharmProjects\pythonDemoqa\photo_5197622001617982831_w.jpg')
        self.element_is_visible(Locators.CURRENT_ADDRESS).send_keys("City, 1231, USA")
        self.element_is_visible(Locators.SUBMIT).click
        self.element_is_visible(Locators.CALENDARY).send_keys("14, February, 2024")
        self.element_is_visible(Locators.CALENDARY).click
        self.driver.find_element(By.XPATH,  "//div[@aria-label='Choose Wednesday, February 14th, 2024']").click()



