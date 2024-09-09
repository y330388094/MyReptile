# 增量式爬虫
# 比如某个网站一定时间会更新一部分内容，有些不会更新，今天我们爬取了网站的所有内容，明天再爬取的时候，我们只需要爬取比昨天新增的内容，原先的不用再爬取，这就是增量式爬虫
# 指定起始url：www.4567tv.tv
# 基于CrawlSpider获取其他页码链接
# 基于Rule将其他页码链接进行请求
# 从每一个页码对应的页面源码中解析出每一个电影详情页的URL
# 核心：检测电影详情页的url之前有没有请求过
# 将爬取过的电影详情页的URL存储
# 存储到redis的set数据结构（自动清楚重复数据，即存在过添加不进去，返回1表示不存在可以添加，返回0表示存在不添加）
# 对详情页的url发起请求，然后解析出电影的名称和简介
# 进行持久化存储

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sunPro.item import SunproItem, DetailItem
from redis import Redis

from scrapy_redis.spiders import RedisCrawlSpider


class SunSpider(RedisCrawlSpider):
    name = "sun"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["http://www.xxx.com/"]
    # 提取详情页链接
    link = LinkExtractor(allow=r"Items/")
    # Rule为规则解析器：将链接提取器提取到的链接进行指定规则(callback)的解析操作
    # Rule参数：链接提取器
    # follow改为True可以将链接提取器 继续作用到 链接提取器提取到的链接 所对应的页面中
    # follow为True可以提取下面显示及未显示页面的所有页码链接
    # follow为False只能提取下面显示的几个页面的链接
    # Rule中的callback调用对应parse_item函数
    rules = (Rule(link, callback="parse_item", follow=True))
    # 创建redis链接对象
    conn = Redis(host='127.0.0.1', port=6379)


    # 当前spider指定pipline
    custom_settings = {
        'ITEM_PIPELINES': {'SunproPipeline': 300, },

    }


    # 如下两个解析方法中是不可以实现请求传参
    # 如果将两个解析方法解析的数据存储到同一个item中，可以依次存储到两个item中，在items.py文件中建两个item类
    def parse_item(self, response):
        # xpath表达式中不可以出现tbgodybiao标签
        tr_list = response.xpath('...')
        for tr in tr_list:
            detail_url = tr.xpath('...').extract_first()
            # 将详情页的url存入redis的set中
            ex = self.conn.sadd('urls', detail_url)
            # ex=1表示数据结构中不存在该url，即没爬取过，可以爬取
            # ex=0表示数据结构中存在该url，即之前爬取过，不用爬取
            if ex == 1:
                print('该url没有被爬取过')
                yield scrapy.Request(url=detail_url, callback=self.parst_detail)
            else:
                print("该url爬取过，还没更新")

    # 解析详情页中的电影名称和类型，进行持久化存储
    def parst_detail(self, response):
        item = SunproItem()
        item['name'] = response.xpath('')
        yield item

