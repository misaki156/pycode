from selenium.webdriver.common.by import By

from Wechat_work.page.base_page import BasePage


class AddMemberPage(BasePage):
    def set_name(self, name):
        name_locator = (By.ID, 'username')
        self.find_element(name_locator).send_keys(name)

    def set_english_name(self, engname):
        eng_name_locator = (By.ID, 'memberAdd_english_name')
        self.find_element(eng_name_locator).send_keys(engname)

    def set_acctid(self, id):
        acctid_locator = (By.ID, 'memberAdd_acctid')
        self.find_element(acctid_locator).send_keys(id)

    def set_sex(self, sex):
        if sex == '男' :
            sex_locator = (By.CSS_SELECTOR, '.ww_radio[value="1"]')
        elif sex == '女' :
            sex_locator = (By.CSS_SELECTOR, '.ww_radio[value="2"]')
        else :
            print('请输入正确的性别（男/女）')
        self.find_element(sex_locator).click()

    def set_phone(self,phone):
        phone_locator = (By.CSS_SELECTOR, '.ww_inputWithTips_WithErr')
        self.find_element(phone_locator).send_keys(phone)

    def press_save_button(self):
        save_button = (By.LINK_TEXT, '保存')
        self.find_element(save_button).click()




