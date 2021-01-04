from selenium import webdriver
import time


Base_url = r'https://www.amazon.com'
PATH = r'D:/Projects/Web_scraping/chromedriver.exe'
ASIN = 'B071CV8CG2'


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(PATH, chrome_options=options)
options.add_argument('--incognito')
options.add_argument('--ignore-certificate-error')

driver.get(Base_url + '/dp/' + ASIN + '?language=en_US')
price1 = driver.find_element_by_xpath('//*[@id="olp-upd-new-used"]/span/a/span[3]').text
print(price1)
time.sleep(3)
driver.quit()