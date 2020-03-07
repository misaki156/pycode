from time import sleep

from selenium.webdriver.common.by import By

from Wechat_work.page.base_page import BasePage


class MaterialPage(BasePage):

    def add_picture(self, pictrue_path):
        pictrue_locator = (By.CSS_SELECTOR, '[href="#material/image"]')
        add_picture_locator = (By.CSS_SELECTOR, '.js_upload_file_selector')
        add_locator = (By.ID, 'js_upload_input')
        #只传一张图片可成功，第二次上传怎么判断完成按钮是否可点击？
        check_sucess_locator = (By.CSS_SELECTOR, '.material_picCard_cnt_pic')
        finish_locator = (By.PARTIAL_LINK_TEXT,'完成')


        self.find_element(pictrue_locator).click()
        self.find_element(add_picture_locator).click()
        self.find_element(add_locator).send_keys(pictrue_path)
        self.wait(10, check_sucess_locator)
        self.find_element(finish_locator).click()



