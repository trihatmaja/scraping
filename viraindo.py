# not yet completed

from scrapy import Spider, Item, Field, Request

def complete_url(string):
    """Return complete url"""
    return "http://www.viraindo.com/" + string

class ViraindoSpider(Spider):
 
    name = 'viraindo_spider'
    start_urls = [
        'http://www.viraindo.com/'
    ]
 
    def parse(self, response):
        links = response.xpath('//a[contains(@href, ".html")]/@href').extract()
        for link in links:
            if (link != "pesan_online.html") :
                yield Request(complete_url(link), callback=self.parse_category)

    def parse_category(self, response):
        items = response.xpath('//tr')
        for item in items:
        #counttd = response.xpath('//tr/td/text()').extract()
        #if(len(counttd)>0):
        #    print counttd[6]
            product = item.xpath('td[1]/text()').extract()[0].strip('\n\t\t')
            price = item.xpath('td[2]/text()').extract()[0].strip('\n\t\t')
            if(product != ""):
                print "%s:%s" %(product, price)