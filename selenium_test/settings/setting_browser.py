import os
from selenium import webdriver


class SettingBrowser:

    @staticmethod
    def get_driver():
        return webdriver.Chrome(os.path.abspath('../drivers/chromedriver.exe'))