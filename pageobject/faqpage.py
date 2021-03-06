from pageobject.base import Base
from pageobject.decorators import web_driver, web_element
from selenium.webdriver.common.by import By


class FAQPage(Base):

    _faq_page_title = (By.CSS_SELECTOR, 'h1')

    @property
    @web_element
    def faq_page_title(self):
        return self._faq_page_title

    @web_driver
    def __init__(self, driver):
        Base.__init__(self, driver)