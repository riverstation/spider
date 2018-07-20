import urllib.request
import urllib.parse

'''
# 直接访问这个页面，肯定是不行的，需要伪造cookie
url = 'http://www.renren.com/960481378/profile'
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

with open('renren.html', 'wb') as fp:
	fp.write(response.read())
'''


# 通过抓包，抓取浏览器访问时候的cookie，通过代码模拟发送即可
'''
url = 'http://www.renren.com/960481378/profile'
headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Connection': 'keep-alive',
	'Cookie': 'anonymid=jjgfrq7uasf0qc; depovince=GW; jebecookies=49de5f46-0b80-490f-9277-f19688fc91a3|||||; _r01_=1; JSESSIONID=abcYl2ngsw4FBhTX16gsw; ick_login=52175eb0-6f30-4f87-b614-91fa81350f73; _de=F872F5698F7602B30ADE65415FC01940; p=42e7d8c2c4c06f39f70b2be38468f15f8; first_login_flag=1; ln_uact=17701256561; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=d34342f75a43ffa1c061400e9126ea118; societyguester=d34342f75a43ffa1c061400e9126ea118; id=960481378; xnsid=79143e47; ver=7.0; loginfrom=null; wp_fold=0; jebe_key=2f649712-9cf8-44a8-8c6a-145cfab423ae%7C86ba94a3b75a9848502e25ac92562959%7C1531272254868%7C1',
	'Host': 'www.renren.com',
	'Referer': 'http://www.renren.com/960481378/profile',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

with open('renren.html', 'wb') as fp:
	fp.write(response.read())
'''