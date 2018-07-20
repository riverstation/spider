import urllib.request
import urllib.error

'''
url = 'http://www.maodan.com/'

try:
	response = urllib.request.urlopen(url)
except Exception as e:
	print(e)
'''

url = 'https://blog.csdn.net/hudeyu777/article/details/76021574'
try:
	response = urllib.request.urlopen(url)
except urllib.error.HTTPError as e:
	print(e)
except urllib.error.URLError as e:
	print(e)

