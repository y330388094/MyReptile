import scrapy


# 定义一个容器来保存要爬取的数据
class MyreptileItem(scrapy.Item):
    # 定义好数据结构，解析返回的html中的数据对应的数据
    title = scrapy.Field()
    url = scrapy.Field()
