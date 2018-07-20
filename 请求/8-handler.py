import urllib.request

url = 'http://www.baidu.com/'
# 创建一个handler
handler = urllib.request.HTTPHandler()
# 根据handler来创建一个opener
opener = urllib.request.build_opener(handler)

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

request = urllib.request.Request(url=url, headers=headers)
# 再往下发送请求操作，都通过opener的open方法，没有urlopen()这个方法了
response = opener.open(request)

print(response.read().decode('utf8'))