import pytest

from selenium_test.settings.setting_browser import SettingBrowser


class TestExample(SettingBrowser):

    @pytest.mark.smoke
    def test_go_to_exist(self):
        driver = self.get_driver()
        driver.maximize_window()
        driver.get('https://exist.ua/')
        driver.close()