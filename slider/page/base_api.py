import os
import sys
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from slider.utils.base_util import BaseUtil


class Base:
    _url = ''

    def __init__(self, driver=None):
        if driver is None:
            browser_env = os.getenv('browser')
            print(f"browser env：{browser_env}")
            if browser_env == 'chrome':
                self.driver = webdriver.Chrome()
            if browser_env == 'ie':
                self.driver = webdriver.Ie()
        else:
            self.driver = driver

        desired = self.driver.desired_capabilities
        # print(f"capas：{desired}")
        browser_version: int = int(desired['browserVersion'].split(".")[0])
        browser_name: str = desired['browserName'].split('.')[0]
        if not BaseUtil.check_version(browser_name=browser_name, browser_version=browser_version):
            print(f'chrome浏览器版本号必须>=82, ie浏览器版本号必须>=11 --> {browser_name}:{browser_version}')
            sys.exit()
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

        if self._url != "":
            self.driver.get(url=self._url)

    def find(self, selector):
        # return self.driver.find_element(*selector)
        if WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(selector)):
            return self.driver.find_element(*selector)
        else:
            print(f'未找到该元素{selector}')
            return False

    def send(self, keys, selector):
        ele = self.find(selector)
        if ele:
            ele.send_keys(keys)

    def close(self):
        self.driver.quit()
