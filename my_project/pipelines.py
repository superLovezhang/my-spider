from itemadapter import ItemAdapter
import json, os


class MyProjectPipeline:
    # 每次spider yield item的时候调用
    def process_item(self, item, spider):
        print("++++++++")
        self.file.write(json.dumps(dict(item)) + '\n')
        return item

    # 打开这个pipeline的时候调用
    def open_spider(self, spider):
        path = os.path.abspath("spiders/data")
        self.file = open('%s\\data.json'%path, 'w', encoding='utf8')
        self.file.write('[\n')

    # 关闭这个pipeline的时候调用
    def close_spider(self, spider):
        self.file.write(']')
        self.file.close()