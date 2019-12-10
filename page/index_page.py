from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class IndexPage(BasePage):
    def __init__(self):
        super().__init__()
        self.denglu = (By.LINK_TEXT,'登录')

    def find_denglu(self):
        return self.driver.find_element(self.denglu)



class IndexHandle(BaseHandle):
    def __init__(self):
        self.index_page = IndexPage()
    def click_denglu(self):
        self.index_page.find_denglu().click()


class IndexProxy:
    def __init__(self):
        self.indexhandle = IndexHandle()
    def to_denglu_page(self):
        self.indexhandle.click_denglu()