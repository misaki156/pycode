from appium.webdriver.common.mobileby import MobileBy

from Xue_qiu.page.base_page import BasePage


class SearchPage(BasePage):
    def search(self, keywords, code):
        search_loc = (MobileBy.ID, 'search_input_text')
        select_loc = (MobileBy.XPATH, '//*[@text="%s"]' %code)
        '''搜索'''
        self.input_element(search_loc, keywords)
        '''点击搜索结果'''
        self.click_element(select_loc)
        return self

    def get_price(self, code):
        code_loc = (MobileBy.XPATH, '//*[@text="%s"]/../../..//*[contains(@resource-id,"current_price")]' %code)
        return float(self.find_element(code_loc).text)
