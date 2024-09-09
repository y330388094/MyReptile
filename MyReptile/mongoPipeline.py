# 处理数据进行数据库插入
# MongoDB 的连接信息还需要定义。我们在 settings.py配置

# setting可以读取配置文件
import pymongo
from scrapy.conf import settings


class MongoPipeline(object):

    def __init__(self, connection_string, database):
        # 方法1------
        self.connection_string = connection_string
        self.database = database


        # 方法2-----
        # 配置MongoDB数据库
        MONGO_HOST = "127.0.0.1"  # 主机IP
        MONGO_PORT = 27017  # 端口号
        MONGO_DB = "smn"  # 库名
        MONGO_COLL = "col_stu"  # collection名
        # 连接数据库
        self.client = pymongo.MongoClient(host=MONGO_HOST, port=MONGO_PORT)
        # 数据库登录需要帐号密码的话
        # self.client.admin.authenticate(settings['MINGO_USER'], settings['MONGO_PSW'])
        self.client = pymongo.MongoClient()
        # 获得数据库的句柄
        self.db = self.client[MONGO_DB]
        # 获得集合collection的句柄
        self.coll = self.db[MONGO_COLL]


    # 标识，这个方法是以依赖注入的方式实现的，方法的参数就是 crawler
    # 通过 crawler，我们能拿到全局配置的每个配置信息，在全局配置 settings.py中，可以通过定义
    # MONGO_URI 和 MONGO_DB来指定MongoDB 连接需要的地址以及数据库名称，拿到配置信息之后返回类对象即可。
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            connection_string=crawler.settings.get('MONGODB_CONNECTION_STRING'),
            database=crawler.settings.get(MONGODB_DATABASE)
        )

    # 当 Spider  被开启时，这个方法被调用，主要进行了一些初始化操作,该方法是框架内置方法，方法名一定不能修改，否则会报错
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.connection_string)
        self.db = self.client[self.database]

    # 方法1-----执行了数据插入操作，这里直接调用 insert方法传入 item  对象即可将数据存储到  MongoDB。
    def process_item(self, item, spider):
        name = item.__class__.__name__
        self.db[name].insert_one(dict(item))
        return item

    # 方法2 -----
    # def process_item(self, item, spider):
    #     self.coll.insert(dict(item))  # 向数据库插入一条记录
    #     return item

    # 当  Spider 被关闭时，这个方法被调用，将数据库连接关闭。
    def close_spider(self, spider):
        self.client.close()

