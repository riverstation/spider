from multiprocessing import Process
import time

class SingProcess(Process):
	def __init__(self, a):
		# 如果要重写构造方法，一定得手动调用父类的构造方法
		super().__init__()
		self.a = a

	def run(self):
		print('传递的参数为%s' % self.a)
		for x in range(1, 5):
			print('我在唱小情歌')
			time.sleep(1)

class DanceProcess(Process):
	def run(self):
		for x in range(1, 5):
			print('我在跳钢管舞')
			time.sleep(1)
		

def main():
	a = '现在很多老歌手为什么不唱歌了'
	p_sing = SingProcess(a)
	# 启动进程，进程启动之后默认执行类里面的run方法
	p_sing.start()

	# p_dance = DanceProcess()
	# p_dance.start()

	p_sing.join()
	# p_dance.join()
	print('主进程结束')

if __name__ == '__main__':
	main()