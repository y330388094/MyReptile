import scrapy

# 引入容器
from MyReptile.items import MyreptileItem

class MyspiderSpider(scrapy.Spider):
    name = "myspider"    # spider 它是每个项目唯一的名字，用来区分不同的 spider
    allowed_domains = ["www.imooc.com"]  # 允许爬取的域名，如果初始或后续的请求链接不是这个域名下的就会被过滤掉
    start_urls = ["https://www.imooc.com"] #  Spider 在启动时进行爬取的 URL 列表，也就是爬虫的起始地址，可以是多个 URL，一般是一个，后续的 URL 则从初始的 URL 获取到的 response 中提取

    # 被调用时，每个初始 URL 完成下载后生成的 Response 对象将会作为唯一的参数传递给该函数。该方法负责解析返回的数据，提取数据（生成 item）以及生成需要进一步处理的 URL 的 Request 对象
    def parse(self, response):
        # 实例化一个容器保存爬取信息
        item = MyreptileItem()
        # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
        # 先获取每个课程的div
        for box in response.xpath('//div[@class="course-card-container"]/a[@target="_blank"]'):
            # 获取div中的课程标题
            # strip() 方法用于移除字符串头尾指定的字符（默认为空格）
            # extract()返回的所有数据，存在一个list里。extract_first()返回的是一个string，是extract()结果中第一个值。
            item['title'] = box.xpath('.//h3/text()').extract()[0].strip()
            # 获取每个div中的课程路径
            item['url'] = 'http://www.imooc.com' + box.xpath('.//@href').extract()[0]

            # 返回信息，把数据交给管道  piplines.py  进行数据的处理
            yield item

        # 下一个链接的采集，比如下一页的内容
        href = response.css("li.next a::attr(href)").extract_first("")
        next_url = response.urljoin(href)
        yield scrapy.Request(url=next_url, callback=self.parse)
