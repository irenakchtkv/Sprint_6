from selenium.webdriver.common.by import By

class OrderPageLocators:

    NAME_FIELD = [By.XPATH, './/input[@placeholder="* Имя"]']  # поле ввода Имя
    SURNAME_FIELD = [By.XPATH, './/input[@placeholder="* Фамилия"]']  # поле ввода Фамилия
    ADDRESS_FIELD = [By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]']  # поле ввода Адрес
    METRO_STATION_FIELD = [By.XPATH, './/input[@placeholder="* Станция метро"]']  # поле ввода станции метро с выпадающим списком
    METRO_STATION_OPTION = []  # вариант станции метро в выпадающем списке
    PHONE_NUMBER_FIELD = [By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]']  # поле ввода номера телефона
    NEXT_BUTTON = [By.XPATH, './/button[text()="Далее"]']  # кнопка Далее

    DELIVERY_DATE_FIELD = [By.XPATH, './/input[@placeholder="* Когда привезти самокат"]']  # поле выбора даты доставки самоката 
    RENTAL_PERIOD_DROPDOWN = [By.XPATH, './/div[text()="* Срок аренды"]']  # выпадающий список с выбором срока аренды
    BLACK_CHECKBOX = [By.ID, 'black']  # чекбокс с выбором черного самоката
    GREY_CHECKBOX = [By.ID, 'grey']  # чекбокс с выбором серого самоката
    COMMENT_FIELD = [By.XPATH, './/input[@placeholder="Комментарий для курьера"]']  # поле для комментария для курьера
    ORDER_BUTTON = [By.XPATH, '(.//button[text()="Заказать"])[2]']  # кнопка Заказать

    CONFIRM_TITLE = [By.XPATH, './/div[text()="Хотите оформить заказ?"]']  # заголовок Хотите оформить заказ?
    YES_BUTTON = [By.XPATH, './/button[text()="Да"]']  # кнопка Да

    ORDER_PLACED_TITLE = [By.XPATH, './/div[text()="Заказ оформлен"]']  # заголовок Заказ оформлен 

    @staticmethod  # метод для формирования локатора с переданным значением 
    def get_rental_period_option(rental_period):

        xpath = f".//div[text()='{rental_period}']"
        return [By.XPATH, xpath]