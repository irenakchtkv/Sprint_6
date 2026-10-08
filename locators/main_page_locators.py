from selenium.webdriver.common.by import By

class MainPageLocators:

    ORDER_BUTTONS = [By.XPATH, './/button[text()="Заказать"]']  # кнопки Заказать
    FAQ_QUESTION_BUTTONS = [By.XPATH, './/div[starts-with(@id, "accordion__heading-")]']  # вопросы FAQ
    FAQ_ANSWER_PANELS = [By.XPATH, './/div[starts-with(@id, "accordion__panel-")]']  # соответствующие ответы
    COOKIE_CONSENT_BUTTON = [By.ID, 'rcc-confirm-button']  # кнопка 'да все привыкли'
    YANDEX_LOGO = [By.XPATH, './/a[@href="//yandex.ru"]']  # логотип-ссылка Яндекса
    SCOOTER_LOGO = [By.XPATH, './/img[@alt="Scooter"]/parent::a']  # логотип-ссылка на главную страницу Яндекс Самокат