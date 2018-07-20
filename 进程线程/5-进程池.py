from multiprocessing import Process
from multiprocessing import Pool
import os
import time

def test(name):
	print('任务%s正在运行,进程id号为%s' % (name, os.getpid()))
	time.sleep(2)

def main():
	# 创建一个进程池对象
	po = Pool(3)

	# 给进程池添加任务
	lt = ['关羽', '赵云', '张飞', '马超', '黄忠', '吕布', '孙策', '大乔']
	for name in lt:
		po.apply_async(test, args=(name, ))

	# 进程池使用完毕之后，关闭
	po.close()
	# 让主进程等待结束
	po.join()
	print('主进程、进程池全部结束')

if __name__ == '__main__':
	main()