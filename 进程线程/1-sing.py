import time

def sing():
	for x in range(1, 5):
		print('我在唱小情歌')
		time.sleep(1)

def dance():
	for x in range(1, 5):
		print('我在跳钢管舞')
		time.sleep(1)

def main():
	sing()
	dance()

if __name__ == '__main__':
	main()