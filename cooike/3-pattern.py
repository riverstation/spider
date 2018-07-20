import re

# 创建正则对象
'''
pattern = re.compile(r'\d{3,5}')
string = '我以前总共谈过1234567次恋爱,我总共结婚7654321次'

# ret = pattern.match(string)
# ret = pattern.search(string)
ret = pattern.findall(string)

print(ret)
'''

'''
pattern = re.compile(r'a(bc){3}')
string = '哈哈呵呵abcbcbcbcbc嘻嘻嘿嘿么么'

ret = pattern.search(string)

print(ret.group())
'''

'''
string = '哈哈<div><span>醉卧沙场君莫笑,古来征战几人回</span></div>嘻嘻'
pattern = re.compile(r'<(\w+)><(\w+)>.+</\2></\1>')

ret = pattern.search(string)

print(ret.group())
'''

'''
string = '<div>两岸猿声啼不住,轻舟已过万重山</div></div></div>'

pattern = re.compile(r'<div>.*?</div>')

ret = pattern.search(string)

print(ret.group())
'''

"""
string = '''english
love is a forever problem
love is feel
'''

pattern = re.compile(r'^love', re.M)

ret = pattern.search(string)
print(ret.group())
"""

"""
string = '''<div>细思极恐
你的对手在看书
你的敌人在磨刀
你的闺蜜在减肥
隔壁老王在练腰
</div>
'''
pattern = re.compile(r'<div>.*</div>', re.S)
ret = pattern.search(string)
print(ret.group())
"""

def fn(ret):
	number = int(ret.group())
	number += 1

	return str(number)

# 正则替换
string = '男人都喜欢19岁的女孩'

pattern = re.compile(r'\d+')

# ret = pattern.sub('40', string)
ret = pattern.sub(fn, string)

print(ret)