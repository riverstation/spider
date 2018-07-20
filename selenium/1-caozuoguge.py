from selenium import webdriver
import time

# 根据webdriver里面的类去创建一个谷歌浏览器对象
path = r'C:\Users\ZBLi\Desktop\1805\day06\ziliao\chromedriver.exe'
browser = webdriver.Chrome(path)

# 再往下，操作浏览器就是操作对象
# 打开百度
url = 'http://www.baidu.com/'
browser.get(url)
time.sleep(2)

# 查找百度输入框
my_input = browser.find_element_by_id('kw')
# 写内容
my_input.send_keys('清纯美女')
time.sleep(2)

# 查找按钮框
button = browser.find_element_by_id('su')
button.click()

time.sleep(3)

# 查找阳光美女链接
href = browser.find_elements_by_xpath('//div[@class="op-img-covers-divide-high"][2]/a[2]')[0]
href.click()
time.sleep(3)

# 推出浏览器
browser.quit()