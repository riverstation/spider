import urllib.request
import urllib.parse

post_url = 'http://fanyi.baidu.com/sug'
# word = input('请输入要查询的英文单词:')
word = 'baby'
# post携带的参数
data = {
	'kw': word
}
# 对post参数进行处理
data = urllib.parse.urlencode(data).encode('utf8')

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}
# 构建请求对象
request = urllib.request.Request(url=post_url, headers=headers)
# 发送请求
response = urllib.request.urlopen(request, data=data)

print(response.read().decode('utf8'))