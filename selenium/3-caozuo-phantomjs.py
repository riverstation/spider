from selenium import webdriver
import time

path = r'C:\Users\ZBLi\Desktop\1805\day06\ziliao\phantomjs-2.1.1-windows\bin\phantomjs.exe'
browser = webdriver.PhantomJS(path)

browser.get('http://www.baidu.com/')
time.sleep(3)

# 拍照片，记录走到哪了
browser.save_screenshot(r'tupian\baidu1.png')

browser.find_element_by_id('kw').send_keys('美女')
time.sleep(2)
browser.find_element_by_id('su').click()
time.sleep(3)

browser.save_screenshot(r'tupian\baidu2.png')

browser.quit()