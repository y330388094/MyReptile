# Scrapy settings for MyReptile project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html


# Scrapy 默认的调度队列是scrapy.pqueues.ScrapyPriorityQueue，它适合做定向爬虫使用，对于通用爬虫，我们应该修改为scrapy.pqueues.DownloaderAwarePriorityQueue
# SCHEDULER_PRIORITY_QUEUE = 'scrapy.pqueues.DownloaderAwarePriorityQueue'

# Scrapy 在做 DNS 解析的时候，是阻塞式的。所以请求量越高，解析 DNS 就会越慢。为了避免这个情况，可以提高线程池的大小。
# REACTOR_THREADPOOL_MAXSIZE = 20

# Scrapy 默认是 DEBUG 级别的日志等级，每次爬取会产生大量的日志。通过把日志等级调整到INFO 可以大大减少日志量。
# LOG_LEVEL = 'INFO'

# 大规模爬虫一般不需要用到 Cookies，所以可以把它禁用。请求失败的自动重试会降低爬虫的速度。但是由于大规模爬虫的爬取范围很大，对于个别失败的请求没有必要重试。
# COOKIES_ENABLED = False
# RETRY_ENABLED = False

# 禁用自动跳转功能，也有助于提高网页访问速度。
# DOWNLOAD_TIMEOUT = 10
# REDIRECT_ENABLED = False


# Scrapy 默认基于深度优先（DFO）搜索算法。但在大规模爬虫中，我们一般会使用广度有限（BFO）搜索算法：
# DEPTH_PRIORITY = 1
# SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
# SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'



# 配置MongoDB数据库
MONGO_HOST = "127.0.0.1"  # 主机IP
MONGO_PORT = 27017  # 端口号
MONGO_DB = "smn"  # 库名
MONGO_COLL = "col_stu"  # collection名



BOT_NAME = "MyReptile"

SPIDER_MODULES = ["MyReptile.spiders"]
NEWSPIDER_MODULE = "MyReptile.spiders"

USER_AGENTS_LIST = [
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"
]


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "MyReptile (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Downloader最大并发请求下载数量
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16   # 每个目标域名最大的并发请求数量，默认8
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "MyReptile.middlewares.MyreptileSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "MyReptile.middlewares.MyreptileDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "MyReptile.pipelines.MyreptilePipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"


# MongoDB 的连接信息
USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
              " Chrome/120.0.0.0 Safari/537.36")

# ROBOTSTXT_OBEY = False  # 修改为False

# 声明了 ITEM_PIPELINES 字典，键名是 Pipeline 的类名称，键值是调用优先级，是一个数字，数字越小则对应的 Pipeline 越先被调用
ITEM_PIPELINES = {
    "MyReptile.pipelines.TestPipeline": 2,
    "MyReptile.pipelines.MongoPipeline": 3,
}
MONGODB_CONNECTION_STRING = "localhost"
MONGODB_DATABASE = "ScrapyQuotes"


DOWNLOADER_MIDDLEWARES = {
    "MyReptile.middlewares.UserAgentMiddleware": 543, # 543是权重值
    'MyReptile.middlewares.CheckUA': 600, # 先执行543权重的中间件，再执行600的中间件
}

# kafka配置
# Kafka的访问ip或者端口（默认localhost:9092）
# KAFKA_IP_PORT = ["192.168.99.1:9092"]
# Kafka的Topic name
# 热卖
# KAFKA_TOPIC_NAME = "ebay_de_hot"
# 默认排序
# KAFKA_TOPIC_NAME = "ebay_us_default"
