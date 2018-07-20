import threading
import time

# 滕王阁序  王勃
# 命硬
# 沁园春-雪
# 出师表

class MyThread(threading.Thread):
	def __init__(self, a):
		super().__init__()
		self.a = a

	def run(self):
		print('传递过来的参数为%s' % self.a)
		for x in range(1, 5):
			print('凤凰台上凤凰游,凤去台空江自流')
			time.sleep(1)

def main():
	a = '落霞与孤鹜齐飞，秋水共长天一色'
	t = MyThread(a)
	t.start()
	t.join()

	print('主线程、子线程全部结束')

if __name__ == '__main__':
	main()