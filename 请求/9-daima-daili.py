import urllib.request

url = 'http://www.baidu.com/s?ie=UTF-8&wd=ip'

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

request = urllib.request.Request(url, headers=headers)

# 101.236.21.22:8866
# 使用代理访问
handler = urllib.request.ProxyHandler(proxies={'http': '101.236.21.22:8866'})
# 根据handler创建opener
opener = urllib.request.build_opener(handler)

response = opener.open(request)

with open('daili.html', 'wb') as fp:
	fp.write(response.read())