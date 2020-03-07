import pytest

from Xue_qiu.page.app import App

search_data = [('alibaba', 'BABA', '200')]

class TestMain:
    def setup(self):
        self.main = App().start().main()

    @pytest.mark.parametrize('keywords,code,price', search_data)
    def test_search(self, keywords, code, price):
        price_result = self.main.goto_search_page().search(keywords, code).get_price(code)
        assert price_result > int(price)

    def teardown(self):
        pass