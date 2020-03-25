from pageobject.homepage import Homepage
from driver.Driver import Driver

class Factory(object):

    homepage = Homepage(Driver.driver)