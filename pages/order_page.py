from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class OrderPage:


    def __init__(self, driver):
        self.driver = driver

    def wait_for_order_page_load(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.url_contains('order'))
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OrderPageLocators.NAME_FIELD))

    def set_name(self, name):
        self.driver.find_element(*OrderPageLocators.NAME_FIELD).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*OrderPageLocators.SURNAME_FIELD).send_keys(surname)

    def set_address(self, address):
        self.driver.find_element(*OrderPageLocators.ADDRESS_FIELD).send_keys(address)

    def click_metro_station_field(self):
        self.driver.find_element(*OrderPageLocators.METRO_STATION_FIELD).click()

    def set_metro_station(self, metro_station):
        self.driver.find_element(*OrderPageLocators.get_metro_station_option(metro_station)).click()

    def set_phone_number(self, phone):
        self.driver.find_element(*OrderPageLocators.PHONE_NUMBER_FIELD).send_keys(phone)

    def click_on_next_button(self):
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()

    def wait_for_next_order_page_section_load(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OrderPageLocators.DELIVERY_DATE_FIELD))

    def set_delivery_date(self, delivery_date):
        self.driver.find_element(*OrderPageLocators.DELIVERY_DATE_FIELD).send_keys(delivery_date)

    def remove_focus_from_delivery_date_field(self):
        self.driver.find_element(*OrderPageLocators.TITLE_ABOUT_RENTAL).click()
    
    def set_rental_period(self, rental_period):
        self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD_DROPDOWN).click()
        self.driver.find_element(*OrderPageLocators.get_rental_period_option(rental_period)).click()

    def set_scooter_color(self, color):
        self.driver.find_element(*OrderPageLocators.get_scooter_color_option(color)).click()

    def click_on_placing_order_button(self):
        self.driver.find_element(*OrderPageLocators.ORDER_BUTTON).click()

    def wait_for_confirm_message_to_appear(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OrderPageLocators.CONFIRM_TITLE))

    def click_on_yes_button(self):
        self.driver.find_element(*OrderPageLocators.YES_BUTTON).click()

    def wait_for_order_successfully_placed_message(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OrderPageLocators.ORDER_PLACED_TITLE))

    def get_success_message_text(self):
        return self.driver.find_element(*OrderPageLocators.ORDER_PLACED_TITLE).text


    def making_an_order(self, order_data):
        self.wait_for_order_page_load()
        self.set_name(order_data['name'])
        self.set_surname(order_data['surname'])
        self.set_address(order_data['address'])
        self.click_metro_station_field()
        self.set_metro_station(order_data['metro_station'])
        self.set_phone_number(order_data['phone'])
        self.click_on_next_button()
        self.wait_for_next_order_page_section_load()
        self.set_delivery_date(order_data['delivery_date'])
        self.remove_focus_from_delivery_date_field()
        self.set_rental_period(order_data['rental_period'])
        self.set_scooter_color(order_data['color'])
        self.click_on_placing_order_button()
        self.wait_for_confirm_message_to_appear()
        self.click_on_yes_button()
        self.wait_for_order_successfully_placed_message()
        return self.get_success_message_text()
