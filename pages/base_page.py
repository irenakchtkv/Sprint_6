from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import urls
import allure

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть главную страницу')
    def open_main_page(self):
        self.driver.get(urls.MAIN_URL)

    @allure.step('Найти элемент')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Найти элементы')
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('Нажать на элемент по локатору')
    def click_on_element(self, locator):
        self.find_element(locator).click()

    @allure.step('Прокрутить до элемента')
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center"});', element)

    @allure.step('Ожидать видимость найденного элемента')
    def wait_visibility_of_element(self, element):
        return WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of(element))

    @allure.step('Получить элемент из списка')
    def find_element_from_list(self, locator, index):
        elements = self.find_elements(locator)
        return elements[index]

    @allure.step('Нажать на найденный элемент')
    def click_on_web_element(self, element):
        element.click()

    @allure.step('Получить текст элемента')
    def get_text_from_element(self, element):
        return element.text


    @allure.step('Ожидать содержание пути в url')
    def wait_for_url_contains_path(self, path):
        return WebDriverWait(self.driver, 3).until(expected_conditions.url_contains(path))

    @allure.step('Ожидать видимость элемента по локатору')
    def wait_for_visibility_of_element_located(self, locator):
        return WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ввести значение')
    def put_value(self, locator, value):
        self.find_element(locator).send_keys(value)

    @allure.step('Ожидать соответствие/равенство url')
    def wait_for_url_to_be(self, url):
        return WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(url))

    @allure.step('Получить текущий url')
    def get_current_url(self):
        return self.driver.current_url


    @allure.step('Ожидать общее количество вкладок, равное двум')
    def wait_for_new_window(self):
        return WebDriverWait(self.driver, 5).until(expected_conditions.number_of_windows_to_be(2))

    @allure.step('Переключиться на другую вкладку')
    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    