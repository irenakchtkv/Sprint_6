from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import urls

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_main_page(self):
        self.driver.get(urls.MAIN_URL)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click_on_element(self, locator):
        self.find_element(locator).click()

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center"});', element)

    def wait_visibility_of_element(self, element):
        return WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of(element))

    def find_element_from_list(self, locator, index):
        elements = self.find_elements(locator)
        return elements[index]

    def click_on_web_element(self, element):
        element.click()

    def get_text_from_element(self, element):
        return element.text



    def wait_for_url_contains_path(self, path):
        return WebDriverWait(self.driver, 3).until(expected_conditions.url_contains(path))

    def wait_for_visibility_of_element_located(self, locator):
        return WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))

    def put_value(self, locator, value):
        self.find_element(locator).send_keys(value)

    def wait_for_url_to_be(self, url):
        return WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(url))

    def get_current_url(self):
        return self.driver.current_url



    def wait_for_new_window(self):
        return WebDriverWait(self.driver, 5).until(expected_conditions.number_of_windows_to_be(2))

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    