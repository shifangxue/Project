from selenium.webdriver.common.by import By

from slider.page.base_api import Base
from slider.page.regedit_page import Regedit


class Main(Base):
    _url = "https://www.ctrip.com/"

    def goto_regedit(self):
        self.find((By.ID, 'nav-bar-set-reg')).click()
        return Regedit(self.driver)
