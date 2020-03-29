from driver.Driver import Driver


def pytest_runtest_setup(item):
    Driver.initialize()

def pytest_runtest_teardown(item):
    Driver.driver.quit()