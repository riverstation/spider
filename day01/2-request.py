import urllib.request

url = 'http://www.baidu.com/'
# 发送请求
# response = urllib.request.urlopen(url)

# print(response.read().decode())
# print(response.readlines())
# print(response.getcode())
# print(response.geturl())
# print(response.getheaders())

# 将响应的内容保存起来, 考虑字符集
# with open('baidu.html', 'w', encoding='utf8') as fp:
# 	fp.write(response.read().decode())

# 不考虑字符集
# with open('baidu1.html', 'wb') as fp:
# 	fp.write(response.read())

# urllib.request.urlretrieve(url=url, filename='./baidu2.html')

# 下载图片的时候
'''
url = 'https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1531122454&di=d7f554b898ae631e5f0a48fe7c35b416&src=http://hbimg.b0.upaiyun.com/225a5f3f75d1d4c59532704782eebd25d323fd801e57a-VlY5c4_fw658'
response = urllib.request.urlopen(url=url)
# 将内容写入到本地
with open('meinv.png', 'wb') as fp:
	fp.write(response.read())
'''
url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1531132953256&di=9aaebbcd124560714010ee2f231a9963&imgtype=0&src=http%3A%2F%2Fimg4.cache.netease.com%2Flady%2F2015%2F3%2F12%2F201503121718011fdaf_550.jpg'
urllib.request.urlretrieve(url, 'shuaige.jpg')