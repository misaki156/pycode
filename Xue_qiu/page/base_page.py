import logging

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    logging.basicConfig(level=logging.INFO)
    _driver: WebDriver
    popup_locs = [(MobileBy.ID, 'com.xueqiu.android:id/tv_agree')]
    '''怎么程序就会进入死循环'''
    # _rerun_max = 5
    # _rerun_count = 0
    def __init__(self, driver: webdriver = None):
        self._driver = driver

    def find_element(self, loc, timeout=10):
        try:
            WebDriverWait(self._driver, timeout).until(expected_conditions.visibility_of_element_located(loc))
            return self._driver.find_element(*loc)
        except:
            for popup_loc in self.popup_locs:
                elements = self._driver.find_elements(*popup_loc)
                if len(elements) > 0:
                    elements[0].click()
                    return self.find_element(loc)




            logging.warning("元素：%s 没找到" % (loc,))

    def click_element(self, loc):
        self.find_element(loc).click()

    def input_element(self, loc, text):
        self.find_element(loc).clear()
        self.find_element(loc).send_keys(text)







