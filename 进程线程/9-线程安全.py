import threading
import time

count = 100
# 创建一把锁
lock = threading.Lock()

def test(number):
	start = time.time()
	# 在这里面修改count的值
	global count
	for x in range(1, 10000000):
		# 加锁
		# lock.acquire()
		count += number
		count -= number
		# 释放锁
		# lock.release()
	end = time.time()
	# 上厕所，大号，如何解决，加锁
	# 用之前，加锁，用完之后，释放锁
	# 牺牲了效率了

	print('循环计算的时间为%s' % (start - end))

def main():
	t1 = threading.Thread(target=test, args=(3, ))
	t2 = threading.Thread(target=test, args=(5, ))
	t2.start()
	t1.start()
	t1.join()
	t2.join()

	print('主线程中打印的count的值为%s' % count)

if __name__ == '__main__':
	main()