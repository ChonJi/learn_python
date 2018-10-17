from selenium import webdriver

browser = webdriver.Chrome(executable_path=r'driver\chromedriver.exe')
browser.get('https://www.expatistan.com/cost-of-living')
print(browser.title)
assert browser.title == 'Cost of Living'

browser.get('http://xxxstwory.pln')
assert browser.find_element_by_xpath('//h1').text == 'Ta witryna jest nieosiągalna'

browser.close()