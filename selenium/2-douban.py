import urllib.request
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action='
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

with open('douban.html', 'wb') as fp:
	fp.write(response.read())

'''
soup = BeautifulSoup(response.read().decode('utf8'), 'lxml')

# 找不到内容
image = soup.select('.movie-list-item > .movie-content > a > img')

print(image)
print(len(image))
'''