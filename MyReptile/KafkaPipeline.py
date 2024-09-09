# 推送数据到kafka

# Scrapy
# from scrapy.conf import settings
from scrapy.utils.project import get_project_settings
# PyKafka
# from pykafka import KafkaClient
from kafka import KafkaProducer
import json


class ScrapyKafkaPipeline(object):
    def __init__(self):
        self.settings = get_project_settings()
        self.producer = KafkaProducer(bootstrap_servers=self.settings['KAFKA_IP_PORT'])

    def process_item(self, item, spider):
        data2 = json.dumps({'product_name': item['product_name'], 'item': item['item'], 'currency': item['currency'],
                            'price': item['price'], 'days7_total_sold': item['days7_total_sold'],
                            'total_sold': item['total_sold'], 'viewed': item['viewed'],
                            'shipping_summary': item['shipping_summary'], 'categroy_id': item['categroy_id'],
                            'start_time': item['start_time'],
                            'product_url': item['product_url'], 'img_url': item['img_url'],
                            'store_name': item['store_name'], 'store_url': item['store_url'],
                            'create_time': item['create_time'], 'ship_country': item["ship_country"],
                            'ship_area': item["ship_area"],
                            'category_url': item["category_url"], 'category_url_page': item["category_url_page"],
                            'is_fire': item["is_fire"]}, sort_keys=True, indent=4, separators=(',', ': '))

        self.producer.send(self.settings['KAFKA_TOPIC_NAME'], bytes(data2, encoding='utf-8'))
        return item

    def close_spider(self, spider):
        self.producer.close()