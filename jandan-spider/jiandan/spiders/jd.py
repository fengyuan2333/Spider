import scrapy
from ..items import JiandanImgItem

class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jdan.net']
    start_urls = ['http://jdan.net/']
    def __init__(self):
        print('''=====目前支持的分类
zoo(动物园)
girl(女装)
ooxx(随手拍)
pond(鱼塘)
===============''')
        self.category=input('请输入类目字段,默认zoo：') or 'zoo'
        self.count=0



    def start_requests(self):
        url='http://jandan.net/%s'%self.category
        yield scrapy.Request(priority=10,dont_filter = True,url=url,callback=self.parse)


    def parse(self,response):

        img_list=response.xpath('//*[@class="text"]/p/a/@href')

        c_count=len(img_list)
        self.count+=c_count
        self.logger.info('总图片数：%s'%self.count)
        for i in img_list:
            imgurl=i.extract()
            item=JiandanImgItem(image_urls=['http:'+imgurl],category=self.category)

            yield item

        next_page=response.xpath('//*[@class="previous-comment-page"]/@href')

        if len(next_page)!=0:
            
            url='http:'+next_page[0].extract()
            #self.logger.info('下一页:%s'%url)
            yield scrapy.Request(priority=10,dont_filter = True,url=url,callback=self.parse)
        else:
            self.logger.info('爬取结束,等待图片下载完成')