import threading
from queue import Queue
import time
from lxml import etree
import requests
import json

# 判断解析线程何时退出的标记位
g_parse_flag = True

class CrawlThread(threading.Thread):
	def __init__(self, name, page_queue, data_queue):
		super().__init__()
		self.name = name
		# 保存页码队列
		self.page_queue = page_queue
		self.data_queue = data_queue
		# url
		self.url = 'http://www.fanjian.net/duanzi-{}'
		self.headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
		}

	def run(self):
		print('%s线程开始启动' % self.name)
		# 这里面的思路是什么？
		while 1:
			if self.page_queue.empty():
				break
			# 1、从页码队列中获取页码
			page = self.page_queue.get()
			# 2、将url和页码进行拼接
			url = self.url.format(page)
			# 3、发送请求，获取响应
			r = requests.get(url=url, headers=self.headers)
			time.sleep(1)
			# 4、将响应内容放入到数据队列中
			self.data_queue.put(r.text)
		print('%s线程结束' % self.name)

class ParseThread(threading.Thread):
	def __init__(self, name, data_queue, lock, fp):
		super().__init__()
		self.name = name
		# 保存数据队列
		self.data_queue = data_queue
		self.lock = lock
		self.fp = fp

	def run(self):
		# time.sleep(3)
		print('%s线程开始启动' % self.name)
		# 解析线程解析步骤
		while 1:
			# 1、从数据队列中取出一个数据
			content = self.data_queue.get()
			# 2、解析这个数据
			items = self.parse_content(content)
			# 3、写入到文件中
			string = json.dumps(items, ensure_ascii=False)
			# 加锁
			self.lock.acquire()
			self.fp.write(string + '====\n')
			# 释放锁
			self.lock.release()

			time.sleep(2)
			if g_parse_flag == False:
				break
		print('%s线程结束' % self.name)

	# 解析数据函数
	def parse_content(self, content):
		# 生成tree对象
		tree = etree.HTML(content)
		# 先找到所有的li标签
		li_list = tree.xpath('//li[@class="cont-item"]')
		items = []
		for oli in li_list:
			# 获取头像
			face = oli.xpath('.//div[@class="cont-list-reward"]//img/@data-src')[0]
			# 获取名字
			name = oli.xpath('.//div[@class="cont-list-head"]/a/text()')[0]
			# 获取内容
			text = oli.xpath('.//div[@class="cont-list-main"]/p/text()')[0]
			# 获取时间
			shijian = oli.xpath('.//div[@class="cont-list-info fc-gray"]/text()')[-1]
			item = {
				'头像': face,
				'名字': name,
				'内容': text,
				'时间': shijian,
			}
			# 将字典添加到列表中
			items.append(item)
		return items
		

def create_queue():
	page_queue = Queue()
	data_queue = Queue()
	# 向页码队列中添加页码
	for page in range(1, 11):
		page_queue.put(page)
	return page_queue, data_queue

def main():
	# 做什么？
	# 创建锁
	lock = threading.Lock()
	# 打开文件
	fp = open('duanzi.txt', 'w', encoding='utf8')
	# 创建两个队列
	page_queue, data_queue = create_queue()
	# 创建采集、解析线程
	crawlname_list = ['采集线程1', '采集线程2', '采集线程3']
	parsename_list = ['解析线程1', '解析线程2', '解析线程3']
	# 列表，用来保存所有的采集线程和解析线程
	t_crawl_list = []
	t_parse_list = []
	for crawlname in crawlname_list:
		t_crawl = CrawlThread(crawlname, page_queue, data_queue)
		t_crawl.start()
		# 将对应的采集线程保存起来
		t_crawl_list.append(t_crawl)

	for parsename in parsename_list:
		t_parse = ParseThread(parsename, data_queue, lock, fp)
		# 将对应的解析线程保存起来
		t_parse_list.append(t_parse)
		t_parse.start()

	# 一直在判断解析线程何时推出
	while 1:
		if page_queue.empty():
			break

	time.sleep(3)
	while 1:
		if data_queue.empty():
			global g_parse_flag
			g_parse_flag = False
			break

	# 让主线程等待子线程结束之后再结束
	for t_crawl in t_crawl_list:
		t_crawl.join()
	for t_parse in t_parse_list:
		t_parse.join()

	fp.close()
	print('主线程、子线程全部结束')

if __name__ == '__main__':
	main()

# 留给大家了，为什么里面没有写数据呢？