import unittest
import time
from pageobject.pagefactory import Factory

class TestHomePage(unittest.TestCase):

    def setUp(self):
        Factory.homepage.go_to_homepage()
        
    def test_list_link(self):
        Factory.homepage.link_list.click()
        assert "List of Books" == Factory.listpage.list_page_title.text
    
    def test_FAQs_link(self):
        Factory.homepage.link_list.click()
        assert "FAQs" in Factory.faqpage.faq_page_title.text