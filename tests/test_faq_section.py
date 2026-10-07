from pages.main_page import MainPage
import pytest
import urls
import data
import allure

class TestFaqSection:


    @pytest.mark.parametrize('faq_index, answer_text', data.FAQ_ANSWERS.items())
    @allure.title('Проверка открытия соответствующего ответа на вопрос с индексом {faq_index}')
    def test_open_faq_answer(self, driver, faq_index, answer_text):
        driver.get(urls.MAIN_URL)

        faq_answer = MainPage(driver)

        actual_text = faq_answer.open_faq_answer(faq_index)

        assert actual_text == answer_text
