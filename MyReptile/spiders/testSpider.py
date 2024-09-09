import scrapy

class testSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['www.httpbin.org']
    start_url = 'https://www.httpbin.org/post'

    data = {"name": "Amo", "age": "18"}

    # 生成Requests对象交给Scrapy下载并返回response
    # 此方法仅能被调用一次，读取start_urls内容并启动循环过程
    def start_requests(self):
        yield scrapy.http.FormRequest(self.start_url, callback=self.parse_response, formdata=self.data)

        yield scrapy.http.JsonRequest(self.start_url, callback=self.parse_response, data=self.data)

    def parse_response(self, response, **kwargs):
        print("text", response.text)