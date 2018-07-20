from lxml import etree

# 将本地的文件生成tree对象
tree = etree.parse('xpath.html')

# ret = tree.xpath('//li[@id="fei"]')
# ret = tree.xpath('//div[@class="mingju"]/ul/li[2]/a')
# ret = tree.xpath('//li[contains(text(),"花")]')
# ret = tree.xpath('//a[starts-with(@class,"y")]/text()')
# ret = tree.xpath('//a[starts-with(@class,"y")]/@href')

ret = tree.xpath('//div[@id="xing"]//text()')
string = '-'.join(ret).replace('\n', '').replace('\t', '')

print(string)