mport allure

from pages.Forms.forms_page import FormsPage

@allure.suite('Elements')
class TestFormsPage(object):
    @allure.feature('Test Forms')
    class TestForms(object):
        @allure.step('Check test form input and output data')
        def test_form_input_and_output_data(self, driver):
            forms_page = FormsPage(driver, 'https://demoqa.com/automation-practice-form')
            forms_page.open()
            p = forms_page.fill_all_fields()
            r = forms_page.form_result()
            assert (p[0] + ' ' + p[1], p[2], p[3]) == (r[0], r[1], r[3]), 'The entered data does not match the result'
