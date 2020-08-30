import os
from selenium import webdriver


class SettingBrowser:
    
    executable_path = {
        "chrome": {
            "windows": os.path.abspath('../drivers/chromedriver.exe'),
            "linux": '/usr/local/bin/chromedriver'
        }
    }

    def get_driver(self):
        return webdriver.Chrome(
            self.executable_path.get('chrome').get('linux')) if os.name == 'posix' else webdriver.Chrome(
                self.executable_path.get('chrome').get('windows'))


