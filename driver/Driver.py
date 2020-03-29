from selenium import webdriver

class Driver(object):

    driver = None

    @classmethod
    def initialize(cls):
        cls.driver = webdriver.Chrome()

    def go_to_homepage(self):
        self.driver.get('http://localhost:4567/apps/pulp/')