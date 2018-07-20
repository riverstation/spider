from bs4 import BeautifulSoup

# 生成soup对象
soup = BeautifulSoup(open('soup.html', encoding='utf8'), 'lxml')
# print(type(soup))

# print(soup.a.attrs)
# print(soup.a.attrs['href'])
# print(soup.a['href'])

# print(soup.a.string)
# print(soup.a.text)
# print(soup.a.get_text())

# print(soup.div.string)
# print(soup.div.text)
# print(soup.div.get_text())

# ret = soup.find('a')
# ret = soup.find('a', title='清明')
# ret = soup.find('a', class_='dumu')
# print(ret)

import re
# ret = soup.find('a', id='xiaoge')
# ret = soup.find('a', id=re.compile(r'^x'))
# print(ret.string)

# ret = soup.find_all('a')
# print(ret[1].string)

# ret = soup.find_all('a', class_='wang')
# print(ret)

# ret = soup.find_all('a', id=re.compile(r'^x'))
# print(ret)

# ret = soup.select('a')
# ret = soup.select('#muxiong')
# print(ret[0]['title'])

# ret = soup.select('.wang')
# print(ret)

# ret = soup.select('div > a')
# print(ret)

# ret = soup.select('a[title=东坡肉]')

# print(ret)

odiv = soup.select('.tang')[0]

ret = odiv.select('a')

print(ret)

'''
class Pig(object):
	"""docstring for Pig"""
	def __str__(self):
		return '我爱可吗'

pig = Pig()
print(pig)
'''
		