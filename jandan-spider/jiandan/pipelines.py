# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.utils.python import to_bytes
import hashlib
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
from scrapy.pipelines.images import ImagesPipeline
from . import settings

class JiandanPipeline:
    def process_item(self, item, spider):
        return item

class ImagesPathPipeline(ImagesPipeline):

    def file_path(self, request, response=None, info=None, *, item=None):

        category=item['category']
        try:
            image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
        except Exception as e:
            print('错误：'e)
        return f'full/{category}/{image_guid}.jpg'
