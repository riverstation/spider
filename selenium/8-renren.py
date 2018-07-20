import requests

# 使用会话技术，首先创建一个会话
# 往下所有操作，使用s进行发送   s.post  s.get
s = requests.Session()

post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018621432232'
data = {
	'email':'17701256561',
	'icode':'',
	'origURL':'http://www.renren.com/home',
	'domain':'renren.com',
	'key_id':'1',
	'captcha_type':'web_login',
	'password':'bd20fe8cf1541a10558676a6eeccb4a1a786cfc09823ddd69d5bbaafc7060292',
	'rkey':'227f4ceb2f44827f9de8296ca1ef1c3f',
	'f':'https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DaovDobnt13PO-vgvw1r-eSnSe_QNvNGtexiQFzyME-a%26wd%3D%26eqid%3Db5d58b1e000297f4000000025b4d88e3',
}
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

r = s.post(url=post_url, headers=headers, data=data)

# print(r.text)

url = 'http://www.renren.com/960481378/profile'

r = s.get(url, headers=headers)

with open('renren.html', 'wb') as fp:
	fp.write(r.content)