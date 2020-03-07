from appium import webdriver

from Xue_qiu.page.base_page import BasePage
from Xue_qiu.page.main_page import MainPage


class App(BasePage):
    _apppackage = 'com.xueqiu.android'
    _appactivity = '.view.WelcomeActivityAlias'

    """初始化driver"""
    def start(self):
        if self._driver is None:
            caps = {}
            caps['platformName'] = 'android'
            caps['platformVersion'] = '6.0'
            caps['deviceName'] = 'Pixel_3_XL_API_23'
            caps['appPackage'] = self._apppackage
            caps['appActivity'] = self._appactivity
            caps['automationName'] = 'uiautomator2'
            caps['chromedriverExecutable'] = 'E:/Python36/Scripts/chromedriver/chromedriver.exe'
            # caps["noReset"] = True

            self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
            self._driver.implicitly_wait(5)
        else:
            self._driver.start_activity(self._apppackage, self._appactivity)
        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self):
        return MainPage(self._driver)