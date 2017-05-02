from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from pago.errors import ExpectedElementError, WaitForElementError
from pago.page import Page
from pago.elements.text import Text
from selenium.webdriver.common.keys import Keys

from laptop import Laptop

page_url = 'http://flipkart.com'

locators = {
    'search_field': ('name', 'q'),
    'suggestions_box': ('class', 'col-11-12'),
    'sorting_options': ('class', '_1No1qI'),
    'popularity': ('xpath', "//li[text()='Popularity']"),
    'product_details': ('class', '_1-2Iqu'),
    'footer': ('class', 'HJlsB9')
}


class FlipkartPage(Page):
    '''Wrapper of a Page object around the Flipkart's site.'''

    def open(self):
        self.driver.get(page_url)
        return self.wait_until_loaded('footer')

    def wait_until_loaded(self, key):
        self.is_available(locators[key])
        return self

    @property
    def title(self):
        return self.driver.title

    def has_search(self):
        '''Checks whether the loaded page has a search bar or not.'''
        return self.is_visible(locators['search_field'])
        
    def search(self, search_text):
        '''Performs search operation on the given `search_text`.'''
        if not self.has_search():
            return self

        search_box = self.find_element_by_locator(locators['search_field'])
        search_box.clear()
        search_box.send_keys(search_text)
        search_box.send_keys(Keys.RETURN)
        return FlipkartPage(self.driver).wait_until_loaded('product_details')

    def has_sorting_options(self):
        '''Checks whether the page has some options for sorting results.'''
        return self.is_visible(locators['sorting_options'])

    def sort_by_popularity(self):
        '''Sorts the results by popularity.'''
        if not self.has_sorting_options():
            return self

        self.find_element_by_locator(locators['popularity']).click()
        return FlipkartPage(self.driver).wait_until_loaded('product_details')
            

    def has_products(self):
        '''Checks if the page has some products on it.'''
        return self.is_visible(locators['product_details'])

    def get_details(self, max_items=5):
        '''Scrapes the products from the first page of the search result.'''
        if self.is_visible(locators['product_details']):
            products = self.find_elements_by_locator(locators['product_details'])
            laptops = [Laptop(p.text) for p in products] # since the search item is laptop
            return laptops
        else:
            return None
