import threading
import os
import time

count = 100

# 该线程用来修改全局变量的值
def change():
	global count
	count += 100
	print('线程%s修改后的值为%s' % (threading.current_thread().name, count))

# 该线程用来读取全局变量的值
def read():
	print('线程%s读取的值为%s' % (threading.current_thread().name, count))


def test():
	a = 100
	name = threading.current_thread().name
	if name == 'lala':
		a += 100
		time.sleep(2)
		print('线程%s修改a的值为%s' % (name, a))
	else:
		time.sleep(5)
		print('线程读取a的值为%s' % a)

def main():
	'''
	t1 = threading.Thread(target=change, name='修改thread')
	t1.start()
	time.sleep(2)

	t2 = threading.Thread(target=read, name='读取thread')
	t2.start()
	'''
	t1 = threading.Thread(target=test, name='lala')
	t2 = threading.Thread(target=test)

	t1.start()
	t2.start()

	t1.join()
	t2.join()

if __name__ == '__main__':
	main()