from pageobject.base import Base
from pageobject.decorators import web_driver, web_element
from selenium.webdriver.common.by import By


class Homepage(Base):

    _pulp_homepage_title = (By.CSS_SELECTOR, 'h1')
    _link_table = (By.CSS_SELECTOR, 'li[id=menu-books-list-table] > a')
    _link_list = (By.CSS_SELECTOR, 'li[id=menu-books-list-list] > a')
    _link_faq = (By.CSS_SELECTOR, 'li[id=menu-books-list-faq] > a')

    @property
    @web_element
    def pulp_homepage_title(self):
        return self._pulp_homepage_title
    
    @property
    @web_element
    def link_table(self):
        return self._link_table
    
    @property
    @web_element
    def link_list(self):
        return self._link_list
    
    @property
    @web_element
    def link_faq(self):
        return self._link_faq

    @web_driver
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_element():
        pass