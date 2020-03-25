import unittest
import time
from pageobject.pagefactory import Factory

class TestHomePage(unittest.TestCase):

    def setUp(self):
        Factory.homepage.go_to_homepage()

    def test_pulper_website(self):
        time.sleep(10)
        pass