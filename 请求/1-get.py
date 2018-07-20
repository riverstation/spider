import urllib.request
import urllib.parse

url = 'https://www.baidu.com/s?'
word = input('请输入要查询的内容:')
# get参数写到这里
data = {
	'ie': 'utf8',
	'wd': word,
}

# 拼接url
query_string = urllib.parse.urlencode(data)

url += query_string

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

# 构建请求对象
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

filename = word + '.html'
# 写入到文件中
with open(filename, 'wb') as fp:
	fp.write(response.read())

# 插件，sublime-repl