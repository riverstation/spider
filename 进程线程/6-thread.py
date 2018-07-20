import threading
import time

def sing(song):
	print('传递过来的参数为%s' % song)
	print('获取线程的名字为%s' % threading.current_thread().name)
	for x in range(1, 5):
		print('我在唱老情歌')
		time.sleep(1)

def dance():
	for x in range(1, 5):
		print('我在跳广场舞')
		time.sleep(1)

def main():
	a = '广岛之恋'
	# 这是一个进程，进程里面有一个主线程，然后主线程创建子线程1（唱歌），子线程2（跳舞）
	t_sing = threading.Thread(target=sing, name='唱歌', args=(a, ))
	t_dance = threading.Thread(target=dance, name='跳舞')

	# 启动线程
	t_sing.start()
	t_dance.start()

	t_sing.join()
	t_dance.join()

	print('主线程、子线程同时结束')

if __name__ == '__main__':
	main()