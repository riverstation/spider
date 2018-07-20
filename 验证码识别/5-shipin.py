import requests
from bs4 import BeautifulSoup
import time
import json
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}


def main():
	url_host = 'http://www.365yg.com'
	url_jiekou = 'http://www.365yg.com/api/pc/feed/?min_behot_time=0&category=video_new&utm_source=toutiao&widen={}&tadrequire=true&as=A1A53B144F2FF2A&cp=5B4FAFEFC23A1E1&_signature=Yt1fHBAXOZY16hdHpfifNWLdXw'

	path = r'C:\Users\ZBLi\Desktop\1805\day06\ziliao\chromedriver.exe'
	browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)

	for page in range(1, 2):
		url = url_jiekou.format(page)
		r = requests.get(url, headers=headers)
		# 响应内容是json数据，需要解析json格式
		obj = json.loads(r.text)
		#　取出所有视频列表 
		shipin_list = obj['data']
		# print(shipin_list)
		for shipin in shipin_list:
			# 拼接视频详情页
			shipin_url = url_host + shipin['source_url']
			# ra = requests.get(url=shipin_url, headers=headers)
			# soup = BeautifulSoup(ra.text, 'lxml')
			print(shipin_url)
			# 使用selenium
			browser.get(shipin_url)
			time.sleep(5)

			with open('dudu.html', 'w', encoding='utf8') as fp:
				fp.write(browser.page_source)
			browser.quit()
			exit()

	


if __name__ == '__main__':
	main()