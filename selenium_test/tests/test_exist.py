import pytest
import requests

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
        assert requests.get('https://exist.ua/').status_code == 200