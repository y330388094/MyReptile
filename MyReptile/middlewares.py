# Define here the models for your spider middleware
# 中间件
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# 定义了Downloader Middlewares和Spider Middlewares的实现
import random

from scrapy import signals

from MyReptile.settings import USER_AGENTS_LIST # 注意导入路径,请忽视pycharm的错误提示
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


# 爬虫中间件主要功能：
# 1、处理引擎传递给爬虫的响应 ,在downloader生成request发送给spider之前，对request进行处理
# 2、处理爬虫传递给引擎的请求, 在spider生成request发送给scheduler之前，对request进行处理
# 3、处理爬虫传递给引擎的数据项, 在spider生成request发送给item pipeline之前，对item进行处理
# 爬虫中间件使用方法和下载中间件相同，且功能重复，通常使用下载中间件
class MyreptileSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)



# 下载器中间件是Scrapy请求/响应处理的钩子框架
# 下载器中间件主要功能：
# 1、添加ip代理
# 2、添加cookie
# 3、添加UA
# 4、请求重试
class MyreptileDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    # 在request通过的时候被调用
    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object, scrapy不会调用其他的process_request或者process_exception直接讲该response作为结果同时会调用process_response函数
        # - or return a Request object scrapy会停止调用process_request并重新调度返回的request
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    # 每次返回结果的时候会自动调用
    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)



# 定义实现随机User-Agent的下载中间件
class UserAgentMiddleware(object):
    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENTS_LIST)
        request.headers['User-Agent'] = user_agent
        # 不写return

class CheckUA:
    def process_response(self, request, response, spider):
        print(request.headers['User-Agent'])
        return response  # 不能少！

# 免费代理ip
# 代理添加的位置：request.meta中增加proxy字段
class ProxyMiddleware1(object):
    def process_request(self, request, spider):
        # proxies可以在settings.py中，也可以来源于代理ip的webapi
        # proxy = random.choice(proxies)

        # 免费的会失效，报 111 connection refused 信息！重找一个代理ip再试
        proxy = 'https://1.71.188.37:3128'

        request.meta['proxy'] = proxy
        return None  # 可以不写return

# 收费代理ip
# 代理隧道验证信息  这个是在那个网站上申请的
import base64
proxyServer = 'http://proxy.abuyun.com:9010'  # 收费的代理ip服务器地址，这里是abuyun
proxyUser = 用户名
proxyPass = 密码
proxyAuth = "Basic " + base64.b64encode(proxyUser + ":" + proxyPass)


class ProxyMiddleware2(object):
    def process_request(self, request, spider):
        # 设置代理
        request.meta["proxy"] = proxyServer
        # 设置认证
        request.headers["Proxy-Authorization"] = proxyAuth


# 检测代理ip是否可用
# 在使用了代理ip的情况下可以在下载中间件的process_response()方法中处理代理ip的使用情况，如果该代理ip不能使用可以替换其他代理ip
class ProxyMiddleware3(object):
    def process_response(self, request, response, spider):
        if response.status != '200':
            request.dont_filter = True  # 重新发送的请求对象能够再次进入队列
            return requst


# UA伪装，代理IP
class MiddleproDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    # UA池
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
        "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    # ip
    PROXY_http = ['153.180.102.104:80', '195.208.131.189:56055']
    PROXY_https = ['120.83.49.90:9000', '95.189.112.214:35508']

    # 拦截请求
    def process_request(self, request, spider):
        # UA伪装
        request.headers['User-Agent'] = random.choice(self.user_agent_list)
        return None

    # 拦截所有响应
    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    # 拦截发送异常请求
    def process_exception(self, request, exception, spider):
        # 当请求IP被禁用，爬取失败，进入到这里
        # 代理
        if request.url.split(':')[0] == 'http':
            request.meta['proxy'] = 'http://' + random.choice(self.PROXY_http)
        else:
            request.meta['proxy'] = 'http://' + random.choice(self.PROXY_https)
        # 将修正之后的请求对象进行重新的请求发送
        return request

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)

