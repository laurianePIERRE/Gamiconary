# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy.exceptions
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrappPipeline:
    def process_item(self, item, spider):
        return item

class DuplicatesPipeline:

    def __init__(self):
        self.seen_items = set()

    def process_item(self, item, spider):
        item_key = item.get('EN', item.get('FR','undefined'))
        if item_key in self.seen_items :
            raise scrapy.exceptions.DropItem(f"Duplicated item found : {item}")
        else :
            self.seen_items.add(item_key)
            return item
