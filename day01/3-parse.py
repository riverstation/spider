import urllib.parse

'''
url = 'http://www.baidu.com/index.html?username=狗蛋&pwd=123'
# url编码
string = urllib.parse.quote(url)
# url解码
lala = urllib.parse.unquote(string)
print(lala)
'''

url = 'http://www.baidu.com/index.html?'
# get参数
data = {
	'username': '狗蛋',
	'pwd': '123',
	'height': '170'
}

string = urllib.parse.urlencode(data)

url += string
print(url)
'''
# 将data拼接为固定的格式放到url的后面
# 遍历字典
lt = []
for k, v in data.items():
	lt.append(k + '=' + v)
query_string = '&'.join(lt)

url += query_string

print(url)
'''