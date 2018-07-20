import urllib.request
import urllib.parse

post_url = 'http://fanyi.baidu.com/v2transapi'

# post参数
formdata = {
	'from': 'en',
	'to': 'zh',
	'query': 'baby',
	'transtype': 'realtime',
	'simple_means_flag': '3',
	'sign': '814534.560887',
	'token': '921cc5d0819e0f1b4212c7fdc3b23866',
}

# 处理表单数据
formdata = urllib.parse.urlencode(formdata).encode('utf8')

headers = {
	'Accept': '*/*',
	# 'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Connection': 'keep-alive',
	# 'Content-Length': '121',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Cookie': 'BAIDUID=59CCBF5477FDC81799054A3DA85BEF88:FG=1; BIDUPSID=59CCBF5477FDC81799054A3DA85BEF88; PSTM=1529815427; pgv_pvi=2975680512; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; locale=zh; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; H_PS_PSSID=1436_26432_21094_20929; PSINO=2; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1531189205,1531202737; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1531202737',
	'Host': 'fanyi.baidu.com',
	'Origin': 'http://fanyi.baidu.com',
	'Referer': 'http://fanyi.baidu.com/?aldtype=16047',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
	'X-Requested-With': 'XMLHttpRequest',
}

# 构建请求对象，发送请求
request = urllib.request.Request(url=post_url, headers=headers)

# 发送请求
response = urllib.request.urlopen(request, data=formdata)

print(response.read().decode('utf-8'))