from multiprocessing import Process
import time
import os

# 想让子进程1执行sing函数
def sing(a):
	print('接受的参数为%s' % a)
	# 进程id号
	print('进程-%s-开始运行' % os.getpid())
	print('父进程为%s' % os.getppid())
	for x in range(1, 5):
		print('我在唱小情歌')
		time.sleep(1)

# 想让子进程2执行dance函数
def dance(a):
	print('进程-%s-开始运行' % os.getpid())
	print('父进程为%s' % os.getppid())
	for x in range(1, 5):
		print('我在跳钢管舞')
		time.sleep(1)

def main():
	# 主进程
	print('主进程id号为%s' % os.getpid())
	a = '青花瓷'
	# 创建进程
	p_sing = Process(target=sing, name='唱歌', args=(a,))
	p_dance = Process(target=dance, name='跳舞', args=(a,))
	
	# 启动进程
	p_sing.start()
	p_dance.start()

	# 获取进程名字
	print(p_sing.name)
	print(p_dance.name)

	# 因为主进程中有子进程的信息，所以主进程必须等子进程结束之后再结束
	p_sing.join()
	p_dance.join()

	print('主进程结束')

if __name__ == '__main__':
	main()