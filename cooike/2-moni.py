import urllib.request
import urllib.parse
import http.cookiejar

# 高级请求cookie的代码实现
# 这个ck对象可以保存cookie
ck = http.cookiejar.CookieJar()
# 根据ck对象创建一个handler
handler = urllib.request.HTTPCookieProcessor(ck)
# 根据handler创建一个opener
opener = urllib.request.build_opener(handler)

# 往下所有的请求都使用opener.open()方法进行发送，这样就会和浏览器的功能一模一样，就是保存cookie并且自动携带cookie发送请求的功能

# 抓包获取到post_url
post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201863950868'
# 表单数据
data = {
	'email': '17701256561',
	'icode': '',
	'origURL': 'http://www.renren.com/home',
	'domain': 'renren.com',
	'key_id': '1',
	'captcha_type': 'web_login',
	'password':	'776f67653bd0b50d6159b7b5173b74249b9e0765da701ff559c986054b9871a7',
	'rkey': 'fe41ddb7ec32db83d8bdbcc6945e267a',
	'f': 'http%3A%2F%2Fwww.renren.com%2F960481378%2Fprofile',
}
data = urllib.parse.urlencode(data).encode('utf8')

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

request = urllib.request.Request(url=post_url, headers=headers)

response = opener.open(request, data=data)


print(response.read().decode('utf8'))
# with open('renren.html', 'wb') as fp:
# 	fp.write(response.read())


# 访问登录后的页面
url = 'http://www.renren.com/960481378/profile'
headers1 = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}
request = urllib.request.Request(url=url, headers=headers1)

response = opener.open(request)

with open('renren.html', 'wb') as fp:
	fp.write(response.read())