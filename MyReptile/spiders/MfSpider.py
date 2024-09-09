import scrapy


class MfspiderSpider(scrapy.Spider):
    name = "MfSpider"

    # 当前spider指定pipline
    custom_settings = {
        'ITEM_PIPELINES': {'pipelineClass1': 300, 'pipelineClass2': 400},

    }

    allowed_domains = ["马蜂窝"]
    start_urls = ["https://马蜂窝"]

    def parse(self, response):
        pass
