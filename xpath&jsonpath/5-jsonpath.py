import json
import jsonpath

fp = open('book.json', 'r', encoding='utf8')
string = fp.read()
fp.close()

# 将json格式字符串转化为python对象
obj = json.loads(string)

# 使用jsonpath
# 查找所有book的author节点内容
# ret = jsonpath.jsonpath(obj, '$.store.book[*].author')

# 从根下面开始找所有的author
ret = jsonpath.jsonpath(obj, '$..author')

# 查找store下面的所有节点
ret = jsonpath.jsonpath(obj, '$.store.*')

# 查找store下面的所有price节点
ret = jsonpath.jsonpath(obj, '$.store..price')

# 查找第三本book
ret = jsonpath.jsonpath(obj, '$..book[2]')

# 查找最后一本书籍
ret = jsonpath.jsonpath(obj, '$..book[(@.length-1)]')
print(ret)