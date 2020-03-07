from appium.webdriver.common.mobileby import MobileBy

from Xue_qiu.page.base_page import BasePage
from Xue_qiu.page.search_page import SearchPage


class MainPage(BasePage):
    def goto_search_page(self):
        search_loc = (MobileBy.ID, 'tv_search')
        self.click_element(search_loc)
        return SearchPage(self._driver)