from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.main_page_locators import MainPageLocators


class MainPage:


    def __init__(self, driver):
        self.driver = driver

    def click_cookie_consent_button(self):
        self.driver.find_element(*MainPageLocators.COOKIE_CONSENT_BUTTON).click()

    def click_order_button(self, index):
        self.driver.find_elements(*MainPageLocators.ORDER_BUTTONS)[index].click()

    def scroll_to_faq_section(self):
        faq_element = self.driver.find_element(*MainPageLocators.FAQ_QUESTION_BUTTONS)
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center"});', faq_element)

    def click_to_question(self, index):
        self.driver.find_elements(*MainPageLocators.FAQ_QUESTION_BUTTONS)[index].click()

    def wait_for_answer_to_appear(self, index):
        faq_answer = self.driver.find_elements(*MainPageLocators.FAQ_ANSWER_PANELS)[index]
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of(faq_answer))

    def get_answer_text(self, index):
        actual_text = self.driver.find_elements(*MainPageLocators.FAQ_ANSWER_PANELS)[index].text
        return actual_text

    def open_faq_answer(self, index):
        self.click_cookie_consent_button()
        self.scroll_to_faq_section()
        self.click_to_question(index)
        self.wait_for_answer_to_appear(index)
        return self.get_answer_text(index)
