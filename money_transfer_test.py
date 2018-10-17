import unittest

from selenium import webdriver


class MoneyTransferTest(unittest.TestCase):

    browser = webdriver.Chrome(executable_path=r'driver\chromedriver.exe')

    #WEB_ELEMENTS
    title = browser.find_element_by_css_selector('title')

    def setUp(self):
        browser = self.browser
        browser.get("http://demo.eurobank.pl/przelew_nowy_zew.html")
        browser.maximize_window()

    def test_money_transfer(self):

        expected_title = 'Eurobank - Bankowość Internetowa - Pulpit'
        title = self.title

        browser = self.browser
        assert title == expected_title


    def tearDown(self):
        browser = self.browser
        browser.close()
