import urllib.request
import urllib.parse
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = 'http://www.baidu.com/'

# 定制请求头部来伪装UA
# response = urllib.request.urlopen(url)
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}
# 构建请求对象
request = urllib.request.Request(url=url, headers=headers)

# 向请求对象发送请求
response = urllib.request.urlopen(request)