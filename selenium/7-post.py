import requests

post_url = 'https://cn.bing.com/ttranslationlookup?&IG=5C360E60322D4FA4865EEBCF710B93B6&IID=translator.5036.2'
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

fromdata = {
	'from': 'zh-CHS',
	'to': 'en',
	'text': '皇上',
}

r = requests.post(url=post_url, data=fromdata, headers=headers)

print(r.text)