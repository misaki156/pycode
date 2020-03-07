from time import sleep

from selenium.webdriver.common.by import By

from Wechat_work.page.add_member_page import AddMemberPage
from Wechat_work.page.base_page import BasePage


class ContactPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    def goto_add_member(self):
        add_mem_locator = (By.CSS_SELECTOR, 'js_add_member')
        self.wait(10, add_mem_locator)
        self.find_element(add_mem_locator).click()
        # self.execute_script(add_mem_locator)
        return AddMemberPage(reuse=True)


