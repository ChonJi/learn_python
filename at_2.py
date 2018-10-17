import unittest
from selenium import webdriver

expected_title = 'Eurobank - Bankowość Internetowa - Logowanie'
expected_title2 = 'Eurobank - Bankowość Internetowa - Lista kont - wiele kont'
expected_title3 = 'Eurobank - Bankowość Internetowa - Pulpit'

class MainTests(unittest.TestCase) :

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=r'driver\chromedriver.exe')
        self.browser.maximize_window()

    def test_demo_login(self):
        browser = self.browser
        browser.get('http://demo.eurobank.pl/logowanie_etap_1.html')
        title = browser.title
        browser.implicitly_wait(20000)
        print(title, ' : ', expected_title)
        assert title == expected_title

    def test_demo_accounts(self):
        browser = self.browser
        browser.get('http://demo.eurobank.pl/konta.html')
        title = browser.title;
        print(title)
        assert title == expected_title2

    def test_demo_pulpit(self):
        browser = self.browser
        browser.get('http://demo.eurobank.pl/pulpit.html')
        title = browser.title
        print(title)
        assert title == expected_title3

    def tearDown(self):
        self.browser.close()