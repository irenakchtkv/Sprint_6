from selenium.webdriver.common.by import By

class MainPageLocators:

    ORDER_BUTTONS = [By.XPATH, './/button[text()="Заказать"]']  # кнопки Заказать
    FAQ_QUESTION_BUTTONS = [By.XPATH, './/div[starts-with(@id, "accordion__heading-")]']  # вопросы FAQ
    FAQ_ANSWER_PANELS = [By.XPATH, './/div[starts-with(@id, "accordion__panel-")]']  # соответствующие ответы