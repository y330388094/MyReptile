import os.path
import sys

from scrapy.crawler import CrawlerProcess
from myspider import myspider
from testSpider import testSpider


def main():
    # 初始化Scrapy爬虫配置参数
    settings = {
        'BOT_NAME': 'mybot',
        'SPIDER_MODULES': ['myspider'],
        'NEWSPIDER_MODULE': 'myspider',
        'ROBOTSTXT_OBEY': True,
    }

    # 创建CrawlerProcess对象
    process = CrawlerProcess(settings)

    # 启动爬虫任务
    process.crawl(MySpider)
    # 启动多个爬虫
    process.crawl(testSpider)

    process.start()


if __name__ == '__main__':
    main()


