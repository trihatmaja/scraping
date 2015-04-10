from scrapy import Spider, Item, Field, Request

class JakartaNotebookSpider(Spider):
 
    name = 'jakartanotebook_spider'
    start_urls = [
        'http://www.jakartanotebook.com/index-product'
    ]
 
    def parse(self, response):
        items = response.xpath('//div[@class="all"]/table/tbody/tr')
        for item in items:
            print item.xpath('td[1]/a/text()').extract() #barang
            print item.xpath('td[2]/a/text()').extract() #harga
            print item.xpath('td[1]/a/@href').extract() #link barang