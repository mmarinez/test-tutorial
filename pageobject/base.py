from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobject.decorators import web_driver
from driver.Driver import Driver

class Base(object):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30

    def go_to_homepage(self):
        Driver.driver.get('http://localhost:4567/apps/pulp/')