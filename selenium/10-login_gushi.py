import requests

# 搞一个会话
s = requests.Session()

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

# 先将验证码下载到本地
get_url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
r = s.get(get_url, headers=headers)

# 需要向图片src发送请求，将验证码下载到本地
image_src = 'https://so.gushiwen.org/RandCode.ashx'
r = s.get(image_src, headers=headers)
with open('code.png', 'wb') as fp:
	fp.write(r.content)


code = input('请输入验证码:')

post_url = 'https://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx'
data = {
	'__VIEWSTATE': 'BvBAwAIKh29BShbC/yKMDsjiElxi+d4wdH3pR2dacgsifqK0rmUzL4Mc9YzHGDc6P6rqB4wMZ39uRj2MpaaSjQtarGnIo6qf1djLGa75XLo/S4b65Uhv2TETKt0=',
	'__VIEWSTATEGENERATOR':'C93BE1AE',
	'from': 'http://so.gushiwen.org/user/collect.aspx',
	'email': '1090509990@qq.com',
	'pwd': '123456',
	'code': code,
	'denglu': '登录',
}

r = s.post(post_url, headers=headers, data=data)

print(r.text)