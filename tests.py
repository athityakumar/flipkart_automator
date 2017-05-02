import time
import unittest

from pago.driver import WebDriver

from flipkartpage import FlipkartPage

class TestFlipkartPage(object):
    '''
    1. Check that the Flipkart's page is loaded. i.e active internet connection existss
    2. 
    '''
    def setup_class(self):
        self.driver = WebDriver()
        self.welcome_page = FlipkartPage(self.driver).open()

    def teardown_class(self):
        self.driver.close()
        self.driver.quit()

    def test_flipkart_welcome(self):
        ''' Check that we have landed on Flipkart's main page.
        '''
        assert 'Flipkart' in self.welcome_page.title
        
    def test_search(self):
        ''' Check the availability of the search bar on the page.
        If the search bar exists, we search for "laptop".
        '''
        assert self.welcome_page.has_search()
        self.search_page = self.welcome_page.search('laptop')

        assert self.search_page.has_sorting_options()
        self.new_search_page = self.search_page.sort_by_popularity()

        assert self.new_search_page.has_products()
        assert self.new_search_page.get_details is not None
        