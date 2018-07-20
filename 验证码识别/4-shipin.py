import requests

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}
url = 'http://v11-tt.ixigua.com/4b01a09e83f0160689371b59c8eb0017/5b500a64/video/m/220b973a6f749d44e809cfed6702d15171e11592b5e000090d816753207/'

r = requests.get(url, headers=headers)

with open('lala.mp4', 'wb') as fp:
	fp.write(r.content)