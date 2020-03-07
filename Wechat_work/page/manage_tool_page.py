from selenium.webdriver.common.by import By

from Wechat_work.page.base_page import BasePage
from Wechat_work.page.material_page import MaterialPage


class ManageToolPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#material/image"

    def goto_material_page(self):
        material_locator = (By.CSS_SELECTOR, '[href="#material/text"]')
        self.find_element(material_locator).click()
        return MaterialPage(reuse=True)
