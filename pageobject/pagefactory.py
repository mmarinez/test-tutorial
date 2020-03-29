from pageobject.homepage import Homepage
from pageobject.tablepage import TablePage
from pageobject.listpage import ListPage
from pageobject.faqpage import FAQPage
from driver.Driver import Driver

class Factory(object):

    homepage = Homepage()
    tablepage = TablePage()
    listpage = ListPage()
    faqpage = FAQPage()