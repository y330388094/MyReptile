# 增量式爬虫管道
from redis import Redis

class SunproPipeline:
    conn = None

    def open_spider(self, spider):
        self.conn = spider.conn

    def process_item(self, item, spider):
        dic = {
            'name': item['name']
        }
        self.conn.lpush('movieData', dic)
        return item
