from pages.order_page import OrderPage
from pages.main_page import MainPage
import pytest
import data
import allure


class TestOrderPage:

    @pytest.mark.parametrize('index, order_data', [(0, data.ORDER_DATA_1), (1, data.ORDER_DATA_2)])
    @allure.title('Проверка успешного оформления заказа самоката')
    def test_making_an_order(self, driver, index, order_data):

        main_page = MainPage(driver)
        main_page.open_main_scooter_page()

        main_page.click_cookie_consent_button()
        main_page.click_order_button(index)

        order_page = OrderPage(driver)

        actual_text = order_page.making_an_order(order_data)

        assert data.SUCCESS_MESSAGE_PART in actual_text