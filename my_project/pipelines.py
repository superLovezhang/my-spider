from itemadapter import ItemAdapter
import json


class MyProjectPipeline:
    # 每次spider yield item的时候调用
    def process_item(self, item, spider):
        print(dict(item), item)

    # 打开这个pipeline的时候调用
    def open_spider(self, spider):
        self.file = open('data.json', 'w', encoding='utf8')

    # 关闭这个pipeline的时候调用
    def close_spider(self, spider):
        self.file.close()