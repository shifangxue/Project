import time

import pytest
from selenium.webdriver.common.by import By

from slider.page.main_page import Main
from slider.page.regedit_page import Regedit


class TestRegedit:

    def setup_class(self):
        self.main = Main()

    def teardown_class(self):
        self.main.close()

    @pytest.mark.parametrize("expect", ['请顺序点击图中文字'])
    def test_regedit(self, expect):
        form = {
            'mobile': '13000000001',
            'valcode': '123456'
        }
        r = self.main.goto_regedit().agree_regedit().regedit(form=form)
        time.sleep(1)
        r.validate_code()
        assert self.main.find((By.CSS_SELECTOR, '.cpt-choose-msg')).__getattribute__('text') == expect
        time.sleep(2)
