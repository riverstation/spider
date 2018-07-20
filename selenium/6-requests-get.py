import requests

'''
url = 'http://www.baidu.com/'
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

r = requests.get(url=url, headers=headers)
'''

# r是响应对象
# 网页的字符串内容
# print(r.text)
# 字节内容
# print(r.content)
# 获取网页的url
# print(r.url)
# 获取响应头部
# print(r.headers)
# 获取状态码
# print(r.status_code)

url = 'https://www.baidu.com/s?'
data = {
	'ie': 'utf8',
	'wd': '周杰伦'
}
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

r = requests.get(url=url, params=data, headers=headers)

with open(r'tupian\zhou.html', 'wb') as fp:
	fp.write(r.content)