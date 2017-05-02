import time
from selenium.common.exceptions import NoAlertPresentException

from pago.errors import WaitForElementError


class Page(object):

    timeout_seconds = 20
    sleep_interval = .25

    def __init__(self, driver):
        self.driver = driver

    @property
    def referrer(self):
        return self.driver.execute_script('return document.referrer')

    def sleep(self, seconds=None):
        if seconds:
            time.sleep(seconds)
        else:
            time.sleep(self.sleep_interval)

    def find_element_by_locator(self, locator):
        return self.driver.find_element_by_locator(locator)

    def find_elements_by_locator(self, locator):
        return self.driver.find_elements_by_locator(locator)

    def is_available(self, locator):
        for i in range(self.timeout_seconds):
            if self.driver.is_element_available(locator):
                break
            self.sleep()
        else:
            raise WaitForElementError('Wait for available timed out')
        return True

    def is_visible(self, locator):
        for i in range(self.timeout_seconds):
            if self.driver.is_visible(locator):
                break
            self.sleep()
        else:
            raise WaitForElementError('Wait for visible timed out')
        return True
