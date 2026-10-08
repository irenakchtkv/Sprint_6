from selenium.webdriver.common.by import By

class OrderPageLocators:

    NAME_FIELD = [By.XPATH, './/input[@placeholder="* Имя"]']  # поле ввода Имя
    SURNAME_FIELD = [By.XPATH, './/input[@placeholder="* Фамилия"]']  # поле ввода Фамилия
    ADDRESS_FIELD = [By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]']  # поле ввода Адрес
    METRO_STATION_FIELD = [By.XPATH, './/input[@placeholder="* Станция метро"]']  # поле ввода станции метро с выпадающим списком
    PHONE_NUMBER_FIELD = [By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]']  # поле ввода номера телефона
    NEXT_BUTTON = [By.XPATH, './/button[text()="Далее"]']  # кнопка Далее

    DELIVERY_DATE_FIELD = [By.XPATH, './/input[@placeholder="* Когда привезти самокат"]']  # поле выбора даты доставки самоката 
    RENTAL_PERIOD_DROPDOWN = [By.XPATH, './/div[text()="* Срок аренды"]']  # выпадающий список с выбором срока аренды
    ORDER_BUTTON = [By.XPATH, '(.//button[text()="Заказать"])[2]']  # кнопка Заказать

    CONFIRM_TITLE = [By.XPATH, './/div[text()="Хотите оформить заказ?"]']  # заголовок Хотите оформить заказ?
    YES_BUTTON = [By.XPATH, './/button[text()="Да"]']  # кнопка Да

    ORDER_PLACED_TITLE = [By.XPATH, './/div[text()="Заказ оформлен"]']  # заголовок Заказ оформлен 

    TITLE_ABOUT_RENTAL = [By.XPATH, './/div[text()="Про аренду"]']  # заголовок Про аренду

    @staticmethod  # метод для формирования локатора с переданным значением 
    def get_rental_period_option(rental_period):

        xpath = f".//div[text()='{rental_period}']"
        return [By.XPATH, xpath]

    @staticmethod  # метод для формирования локатора с переданным значением 
    def get_scooter_color_option(color):

        return [By.ID, color]

    @staticmethod  # метод для формирования локатора с переданным значением 
    def get_metro_station_option(metro_station):
    
        xpath = f".//div[text()='{metro_station}']"
        return [By.XPATH, xpath]
    