from Wechat_work.page.contact_page import ContactPage

member_info = ['兔斯基', '156', '女', '17012345678']

class TestContact:

    def setup(self):
        self.contact = ContactPage(reuse=True)

    def test_add_member(self):
        self.contact.goto_add_member().set_name(member_info[0])
        self.contact.goto_add_member().set_acctid(member_info[1])
        self.contact.goto_add_member().set_sex(member_info[2])
        self.contact.goto_add_member().set_phone(member_info[3])
        self.contact.goto_add_member().press_save_button()