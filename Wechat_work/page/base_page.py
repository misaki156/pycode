from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _base_url = ""

    def __init__(self, reuse=False):
        if reuse:
            options = webdriver.ChromeOptions()
            options.debugger_address = '127.0.0.1:9222'
            self._driver = webdriver.Chrome(options=options)

        else:
            self._driver = webdriver.Chrome()

        if self._base_url != "":
            self._driver.get(self._base_url)
        self._driver.implicitly_wait(3)

    def find_element(self, by, locator=""):
        if isinstance(by, tuple):
            return self._driver.find_element(*by)
        else:
            return self._driver.find_element(by, locator)

    def find_elements(self, by, locator=""):
        if isinstance(by, tuple):
            return self._driver.find_elements(*by)
        else:
            return self._driver.find_elements(by, locator)

    def wait(self, timeout, locator: tuple):
        return WebDriverWait(self._driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

    def execute_script(self, locator):
        self._driver.execute_script("arguments[0].click;", self.find_element(locator))


