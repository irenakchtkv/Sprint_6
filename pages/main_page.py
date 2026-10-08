from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import urls

class MainPage(BasePage):

    def open_main_scooter_page(self):
        self.open_main_page()

    def click_cookie_consent_button(self):
        self.click_on_element(MainPageLocators.COOKIE_CONSENT_BUTTON)

    def click_order_button(self, index):
        order_button = self.find_element_from_list(MainPageLocators.ORDER_BUTTONS, index)
        self.click_on_web_element(order_button)

    def scroll_to_faq_section(self):
        self.scroll_to_element(MainPageLocators.FAQ_QUESTION_BUTTONS)

    def click_to_question(self, index):
        question = self.find_element_from_list(MainPageLocators.FAQ_QUESTION_BUTTONS, index)
        self.click_on_web_element(question)

    def wait_for_answer_to_appear(self, index):
        faq_answer = self.find_element_from_list(MainPageLocators.FAQ_ANSWER_PANELS, index)
        self.wait_visibility_of_element(faq_answer)

    def get_answer_text(self, index):
        faq_answer = self.find_element_from_list(MainPageLocators.FAQ_ANSWER_PANELS, index)
        return self.get_text_from_element(faq_answer)

    def open_faq_answer(self, index):
        self.open_main_scooter_page()
        self.click_cookie_consent_button()
        self.scroll_to_faq_section()
        self.click_to_question(index)
        self.wait_for_answer_to_appear(index)
        return self.get_answer_text(index)


    def click_scooter_logo(self):
        self.click_on_element(MainPageLocators.SCOOTER_LOGO)
    
    def wait_for_load_main_scooter_page(self):
        self.wait_for_url_to_be(urls.MAIN_URL)

    def go_to_main_scooter_page(self):
        self.click_scooter_logo()
        self.wait_for_load_main_scooter_page()
        return self.get_current_url()


    def click_yandex_logo(self):
        self.click_on_element(MainPageLocators.YANDEX_LOGO)
    
    def wait_for_new_tab_to_appear(self):
        self.wait_for_new_window()

    def switch_to_new_tab(self):
        self.switch_to_new_window()

    def wait_for_load_dzen_page(self):
        self.wait_for_url_contains_path(urls.DZEN_DOMAIN)

    def go_to_dzen_new_tab(self):
        self.click_yandex_logo()
        self.wait_for_new_tab_to_appear()
        self.switch_to_new_tab()
        self.wait_for_load_dzen_page()
        return self.get_current_url()