from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import urls
import allure

class MainPage(BasePage):

    @allure.step('Открыть главную страницу Самоката')
    def open_main_scooter_page(self):
        self.open_main_page()

    @allure.step('Закрыть уведомление об использовании cookie')
    def click_cookie_consent_button(self):
        self.click_on_element(MainPageLocators.COOKIE_CONSENT_BUTTON)

    @allure.step('Нажать на кнопку Заказать')
    def click_order_button(self, index):
        order_button = self.find_element_from_list(MainPageLocators.ORDER_BUTTONS, index)
        self.click_on_web_element(order_button)

    @allure.step('Прокрутить до раздела Вопросы о важном')
    def scroll_to_faq_section(self):
        self.scroll_to_element(MainPageLocators.FAQ_QUESTION_BUTTONS)

    @allure.step('Нажать на вопрос')
    def click_to_question(self, index):
        question = self.find_element_from_list(MainPageLocators.FAQ_QUESTION_BUTTONS, index)
        self.click_on_web_element(question)

    @allure.step('Дождаться развертывания ответа')
    def wait_for_answer_to_appear(self, index):
        faq_answer = self.find_element_from_list(MainPageLocators.FAQ_ANSWER_PANELS, index)
        self.wait_visibility_of_element(faq_answer)

    @allure.step('Получить текст ответа')
    def get_answer_text(self, index):
        faq_answer = self.find_element_from_list(MainPageLocators.FAQ_ANSWER_PANELS, index)
        return self.get_text_from_element(faq_answer)

    @allure.step('Открыть ответ на вопрос')
    def open_faq_answer(self, index):
        self.open_main_scooter_page()
        self.click_cookie_consent_button()
        self.scroll_to_faq_section()
        self.click_to_question(index)
        self.wait_for_answer_to_appear(index)
        return self.get_answer_text(index)

    @allure.step('Нажать на логотип Самоката')
    def click_scooter_logo(self):
        self.click_on_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step('Дождаться загрузки главной страницы')
    def wait_for_load_main_scooter_page(self):
        self.wait_for_url_to_be(urls.MAIN_URL)

    @allure.step('Перейти на главную страницу')
    def go_to_main_scooter_page(self):
        self.open_main_scooter_page()
        self.click_scooter_logo()
        self.wait_for_load_main_scooter_page()
        return self.get_current_url()

    @allure.step('Нажать на логотип Яндекса')
    def click_yandex_logo(self):
        self.click_on_element(MainPageLocators.YANDEX_LOGO)

    @allure.step('Дождаться появления новой вкладки')
    def wait_for_new_tab_to_appear(self):
        self.wait_for_new_window()

    @allure.step('Переключиться на новую вкладку')
    def switch_to_new_tab(self):
        self.switch_to_new_window()

    @allure.step('Дождаться загрузки страницы Дзена')
    def wait_for_load_dzen_page(self):
        self.wait_for_url_contains_path(urls.DZEN_DOMAIN)

    @allure.step('Перейти на страницу Дзена в новой вкладке')
    def go_to_dzen_new_tab(self):
        self.open_main_scooter_page()
        self.click_yandex_logo()
        self.wait_for_new_tab_to_appear()
        self.switch_to_new_tab()
        self.wait_for_load_dzen_page()
        return self.get_current_url()