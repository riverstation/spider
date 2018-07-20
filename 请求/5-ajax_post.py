import urllib.request
import urllib.parse

post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
data = {
	'cname': '石河子',
	'pid': '',
	'pageIndex': '1',
	'pageSize': '10',
}
# 处理data数据
data = urllib.parse.urlencode(data).encode('utf8')
# 
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}
request = urllib.request.Request(url=post_url, headers=headers)

response = urllib.request.urlopen(request, data=data)

print(response.read().decode())