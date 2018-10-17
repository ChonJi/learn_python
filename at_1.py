from selenium import webdriver
import at_2

expected_title = at_2.expected_title

browser = webdriver.Chrome(executable_path=r'driver\chromedriver.exe')
browser.maximize_window()
browser.get('http://demo.eurobank.pl/logowanie_etap_1.html')
title = browser.title
browser.implicitly_wait(20000)
print(title,' : ',expected_title)
assert title == expected_title
browser.close()




