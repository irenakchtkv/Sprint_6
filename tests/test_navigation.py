from pages.base_page import BasePage
import urls

class TestNavigation:

    def test_go_to_main_scooter_page(self, driver):

        driver.get(urls.MAIN_URL)

        scooter_navi = BasePage(driver)

        assert scooter_navi.go_to_main_scooter_page() == urls.MAIN_URL

    def test_go_to_dzen_new_tab(self, driver):

        driver.get(urls.MAIN_URL)

        dzen_navi = BasePage(driver)

        assert urls.DZEN_DOMAIN in dzen_navi.go_to_dzen_new_tab()
