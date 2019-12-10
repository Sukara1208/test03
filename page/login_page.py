from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.username = (By.ID,'username')
        self.password = (By.ID,'password')
        self.verify_code = (By.ID,'verify_code')
        self.sbtbutton = (By.NAME,'sbtbutton')
    def find_username(self):
        return self.find_element(self.username)
    def find_password(self):
        return self.find_element(self.password)
    def find_verify_code(self):
        return self.find_element(self.verify_code)
    def find_sbtbutton(self):
        return self.find_element(self.sbtbutton)

class LoginHandle(BaseHandle):
    def __init__(self):
        self.login_page = LoginPage()

    def input_username(self,username):
        self.input_text(self.login_page.find_username(),username)
    def input_password(self,password):
        self.input_text(self.login_page.find_password(),password)
    def input_verify_code(self,verify_code):
        self.input_text(self.login_page.find_verify_code(),verify_code)
    def click_sbtbutton(self):
        self.login_page.find_sbtbutton().click()

class LoginProxy:
    def __init__(self):
        self.login_handle = LoginHandle()

    def login(self,username,password,verify_code):
        self.login_handle.input_username(username)
        self.login_handle.input_password(password)
        self.login_handle.input_verify_code(verify_code)
        self.login_handle.click_sbtbutton()
