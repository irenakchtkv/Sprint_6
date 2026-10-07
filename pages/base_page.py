from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators
import urls


class BasePage:


    def __init__(self, driver):
        self.driver = driver

    def click_scooter_logo(self):
        self.driver.find_element(*BasePageLocators.SCOOTER_LOGO).click()

    def wait_for_load_main_scooter_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(urls.MAIN_URL))
    
    def go_to_main_scooter_page(self):
        self.click_scooter_logo()
        self.wait_for_load_main_scooter_page()
        return self.get_current_url()



    def click_yandex_logo(self):
        self.driver.find_element(*BasePageLocators.YANDEX_LOGO).click()

    def wait_for_new_tab_to_appear(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.number_of_windows_to_be(2))

    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def wait_for_load_dzen_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.url_contains(urls.DZEN_DOMAIN))

    def go_to_dzen_new_tab(self):
        self.click_yandex_logo()
        self.wait_for_new_tab_to_appear()
        self.switch_to_new_tab()
        self.wait_for_load_dzen_page()
        return self.get_current_url()
    

    def get_current_url(self):
        return self.driver.current_url