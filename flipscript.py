import sys

from pago.driver import WebDriver
from flipkartpage import FlipkartPage

def main():
    ''' The main script to perform the task.'''
    # Setting up the driver and loading Flipkart's landing page
    driver = WebDriver()
    welcome_page = FlipkartPage(driver).open()

    # Searching for "laptop"
    search_page = welcome_page.search('laptop')
    # Sorting the results by Popularity
    new_search_page = search_page.sort_by_popularity()
    # Printing a list of most popular laptops
    laptops = new_search_page.get_details(max_items=5)
    for i, laptop in enumerate(laptops):
        print('--------------------------------------\n')
        print(i+1, laptop)
        print('--------------------------------------\n')

    # Tearing down the setup
    driver.close()
    driver.quit()

if __name__ == '__main__':
    main()
