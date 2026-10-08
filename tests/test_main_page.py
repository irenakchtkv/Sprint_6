from pages.main_page import MainPage
import pytest
import data
import allure
import urls

class TestMainPage:


    @pytest.mark.parametrize('faq_index, answer_text', data.FAQ_ANSWERS.items())
    @allure.title('Проверка открытия соответствующего ответа на вопрос с индексом {faq_index}')
    def test_open_faq_answer(self, driver, faq_index, answer_text):
        
        main_page = MainPage(driver)

        actual_text = main_page.open_faq_answer(faq_index)

        assert actual_text == answer_text

    @allure.title('Проверка перехода на главную страницу Самоката при нажатии на логотип Самоката')
    def test_go_to_main_scooter_page(self, driver):
    
        main_page = MainPage(driver)
    
        assert main_page.go_to_main_scooter_page() == urls.MAIN_URL
    
    @allure.title('Проверка перехода на страницу Дзена при нажатии на логотип Яндекса')
    def test_go_to_dzen_new_tab(self, driver):
    
        main_page = MainPage(driver)
    
        assert urls.DZEN_DOMAIN in main_page.go_to_dzen_new_tab()
    
