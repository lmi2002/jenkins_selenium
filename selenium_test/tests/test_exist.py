import pytest
import requests
import allure

from selenium_test.settings.setting_browser import SettingBrowser


class TestExample(SettingBrowser):

    @pytest.mark.smoke
    def test_go_to_exist(self):
        driver = self.get_driver()
        driver.fullscreen_window()
        driver.get('https://exist.ua/')
        driver.close()

    @pytest.mark.api
    def test_exist(self):
        with allure.step('Request'):
            assert requests.get('https://exist.ua/').status_code == 200

    @pytest.mark.api
    @allure.feature('check Api')
    @allure.story('status code')
    def test_ukrnet(self):
        with allure.step('Request'):
            assert requests.get('https://www.ukr.net/').status_code == 200

    @pytest.mark.api
    @allure.feature('check Api')
    @allure.story('status code')
    def test_invalid(self):
        r = False
        assert r