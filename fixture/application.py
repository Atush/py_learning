from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.manager import ManageHelper

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(5)
        self.manager = ManageHelper(self)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")


    def destroy(self):
        self.wd.quit()