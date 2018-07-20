from selenium import webdriver
import time

path = r'C:\Users\ZBLi\Desktop\1805\day06\ziliao\phantomjs-2.1.1-windows\bin\phantomjs.exe'
browser = webdriver.PhantomJS(path)

url = 'https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action='
browser.get(url)
time.sleep(3)
browser.save_screenshot(r'tupian\douban1.png')

# 执行一句js代码即可
# for x in range(1, 6):
# 	js = 'document.body.scrollTop=10000'
# 	browser.execute_script(js)
# 	time.sleep(3)
# 	browser.save_screenshot(r'tupian\douban2.png')

js = 'document.body.scrollTop=10000'
browser.execute_script(js)
time.sleep(3)

# 获取执行js之后的网页代码
with open(r'tupian\douban.html', 'w', encoding='utf8') as fp:
	fp.write(browser.page_source)

# 往下就可以通过bs或者xpath来解析网页内容了

# 模拟点击加载更多，就是通过browser找到那个按钮，让按钮执行click方法即可

browser.quit()