import urllib.request
import urllib.parse

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'

print('每页显示20条数据')
# page = input('请输入要第几页数据:')
page = 3

# 根据page就可以计算出来start和limit的值
start = (page-1) * 20
limit = 20

# 写get参数
data = {
	'start': start,
	'limit': limit,
}

# 将字典转化为query_string格式
query_string = urllib.parse.urlencode(data)

# 拼接url
url += query_string

# print(url)
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

print(response.read().decode('utf8'))