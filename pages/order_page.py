import urls
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure


class OrderPage(BasePage):

    @allure.step('Дождаться загрузки страницы заказа по url и полю ввода имени')
    def wait_for_order_page_load(self):
        self.wait_for_url_contains_path(urls.ORDER_PATH)
        self.wait_for_visibility_of_element_located(OrderPageLocators.NAME_FIELD)

    @allure.step('Ввести имя')
    def set_name(self, name):
        self.put_value(OrderPageLocators.NAME_FIELD, name)

    @allure.step('Ввести фамилию')
    def set_surname(self, surname):
        self.put_value(OrderPageLocators.SURNAME_FIELD, surname)

    @allure.step('Ввести адрес')
    def set_address(self, address):
        self.put_value(OrderPageLocators.ADDRESS_FIELD, address)

    @allure.step('Нажать на поле ввода станции метро')
    def click_metro_station_field(self):
        self.click_on_element(OrderPageLocators.METRO_STATION_FIELD)

    @allure.step('Указать станцию метро')
    def set_metro_station(self, metro_station):
        self.click_on_element(OrderPageLocators.get_metro_station_option(metro_station))

    @allure.step('Ввести номер телефона')
    def set_phone_number(self, phone):
        self.put_value(OrderPageLocators.PHONE_NUMBER_FIELD, phone)

    @allure.step('Нажать на кнопку Далее')
    def click_on_next_button(self):
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Дождаться появления следующего этапа заказа самоката')
    def wait_for_next_order_page_section_load(self):
        self.wait_for_visibility_of_element_located(OrderPageLocators.DELIVERY_DATE_FIELD)

    @allure.step('Указать дату доставки')
    def set_delivery_date(self, delivery_date):
        self.put_value(OrderPageLocators.DELIVERY_DATE_FIELD, delivery_date)

    @allure.step('Убрать фокус с поля ввода даты доставки')
    def remove_focus_from_delivery_date_field(self):
        self.click_on_element(OrderPageLocators.TITLE_ABOUT_RENTAL)

    @allure.step('Указать срок аренды')
    def set_rental_period(self, rental_period):
        self.click_on_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.click_on_element(OrderPageLocators.get_rental_period_option(rental_period))

    @allure.step('Указать цвет самоката')
    def set_scooter_color(self, color):
        self.click_on_element(OrderPageLocators.get_scooter_color_option(color))

    @allure.step('Нажать на кнопку Заказать')
    def click_on_placing_order_button(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Дождаться появления окна с вопросом о подтверждении заказа')
    def wait_for_confirm_message_to_appear(self):
        self.wait_for_visibility_of_element_located(OrderPageLocators.CONFIRM_TITLE)

    @allure.step('Нажать на кнопку Да')
    def click_on_yes_button(self):
        self.click_on_element(OrderPageLocators.YES_BUTTON)

    @allure.step('Дождаться сообщения об успешном оформлении заказа')
    def wait_for_order_successfully_placed_message(self):
        self.wait_for_visibility_of_element_located(OrderPageLocators.ORDER_PLACED_TITLE)

    @allure.step('Получить текст сообщения об успешном оформлении заказа')
    def get_success_message_text(self):
        element = self.find_element(OrderPageLocators.ORDER_PLACED_TITLE)
        return self.get_text_from_element(element)


    @allure.step('Оформить заказ')
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
