
# Item Pipeline 为项目管道，当 Item 生成后，它会自动发送到 Item Pipeline 处进行处理，我们可以用 Item Pipeline 来做如下操作：
#
# 清洗 HTML 数据
# 验证爬取数据，检查爬取字段
# 查重并丢弃重复内容
# 将爬取结果存储到数据库

class testPipeline(object):

    def __init__(self):
        self.limit = 50

    def process_item(self, item, spider):
        if item['title']:
            if len(item['title']) > self.limit:
                item['title'] = item['title'][:self.limit].rstrip() + '...'

            return item
        else:
            return DropItem('Missing Text')
