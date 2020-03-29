from driver.Driver import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def web_driver(original_func):
    def wrapper(self, *args, **kwargs):
        return original_func(self, Driver.driver, *args, **kwargs)
    
    return wrapper


def web_element(original_func):
    def wrapper(*args, **kwargs):
        _web_element = WebDriverWait(Driver.driver, 10).until(
            EC.visibility_of_element_located(
                original_func(*args, **kwargs)
            )
        )

        return _web_element
    return wrapper