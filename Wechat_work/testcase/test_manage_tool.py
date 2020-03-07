import pytest

from Wechat_work.page.manage_tool_page import ManageToolPage
from Wechat_work.utils.common import get_file_abspath

picture_path = ['../data/zhemu.png']

class TestManageTool:
    def setup(self):
        self.manage_tool_page = ManageToolPage(reuse=True)

    @pytest.mark.parametrize('upload_pic_path', picture_path)
    def test_material(self, upload_pic_path):
        self.manage_tool_page.goto_material_page().add_picture(get_file_abspath(upload_pic_path))
        #怎么写断言？
