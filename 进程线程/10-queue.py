from queue import Queue

# 创建一个队列
# 如果写，代表队列的长度，如果不写，队列长度无限
q = Queue(5)

print(q.empty())
print(q.full())
print(q.qsize())

# 向队列中添加数据
q.put('吴彦祖')
q.put('岳云鹏')
q.put('王宝强')
q.put('黄渤')
q.put('刘德华')
print(q.empty())
print(q.full())
print(q.qsize())
# q.put('古天乐', True, 5)

# 从队列中获取数据
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
# print(q.get(True, 5))