from selenium import webdriver

import time

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

path = r'C:\Users\ZBLi\Desktop\1805\day06\ziliao\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)

browser.get('http://www.baidu.com/')
time.sleep(2)

browser.save_screenshot(r'tupian\baidu3.png')

browser.quit()