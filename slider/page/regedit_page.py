import time

import pytesseract as pytesseract
from PIL import Image
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from slider.page.base_api import Base


class Regedit(Base):

    def agree_regedit(self):
        self.find((By.CSS_SELECTOR, '.reg_agree')).click()
        return self

    def regedit(self, form):
        self.send(form['mobile'], (By.ID, 'mobilephone'))
        self._drag((By.CSS_SELECTOR, ".cpt-drop-btn"))
        self.send(form['valcode'], (By.ID, 'valcode'))
        return self

    def _drag(self, selector):
        # 点击滑块
        ele = self.find(selector)
        ele.click()
        slide = self.find((By.ID, 'slideCode'))
        action = ActionChains(self.driver)
        x = slide.size['width']
        y = slide.location['y']
        action.drag_and_drop_by_offset(ele, xoffset=x, yoffset=y)
        action.perform()

    def validate_code(self):
        verity_code1 = Image.open('..//img//1.jpg')
        verity_code2 = Image.open('..//img//2.jpg')
        verity_code3 = Image.open('..//img//3.jpg')
        time.sleep(1)
        code1 = pytesseract.image_to_string(verity_code1)
        code2 = pytesseract.image_to_string(verity_code2)
        code3 = pytesseract.image_to_string(verity_code3)
        print(f'code_english={code1}, code_zh={code2}, code={code3}')
