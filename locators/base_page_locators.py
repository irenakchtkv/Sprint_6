from selenium.webdriver.common.by import By

class BasePageLocators:

    YANDEX_LOGO = [By.XPATH, './/a[@href="//yandex.ru"]']  # логотип-ссылка Яндекса
    SCOOTER_LOGO = [By.XPATH, './/img[@alt="Scooter"]/parent::a']  # логотип-ссылка на главную страницу Яндекс Самокат