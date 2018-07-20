from multiprocessing import Process
import os
import time

count = 100

# 该进程用来修改全局变量的值
def change():
	global count
	count += 100
	print('进程%s修改后的值为%s' % (os.getpid(), count))

# 该进程用来读取全局变量的值
def read():
	print('进程%s读取的值为%s' % (os.getpid(), count))

def test(c):
	a = 100
	if c == 'hello':
		a += 100
		time.sleep(2)
		print('进程%s修改a的值为%s' % (os.getpid(), a))
	else:
		time.sleep(5)
		print('进程%s读取a的值为%s' % (os.getpid(), a))

def main():
	'''
	p1 = Process(target=change)
	p1.start()
	time.sleep(2)

	p2 = Process(target=read)
	p2.start()
	'''
	a = 'hello'
	b = 'world'
	p1 = Process(target=test, args=(a, ))
	p2 = Process(target=test, args=(b, ))
	p1.start()
	p2.start()

	p1.join()
	p2.join()

if __name__ == '__main__':
	main()