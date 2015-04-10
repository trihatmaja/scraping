from scrapy import Spider, Item, Field, Request

def complete_url(string):
    """Return complete url"""
    return "http://www.bhinneka.com" + string

class BhinnekaSpider(Spider):
 
    name = 'bhinneka_spider'
    start_urls = [
        'http://www.bhinneka.com/categories.aspx'
    ]
 
    def parse(self, response):
        items = response.xpath('//div[@id="ctl00_content_divContent"]//li[@class="item"]/a[2]/@href')
        for item in items:
            link = item.extract()
            yield Request(complete_url(link), callback=self.parse_category)

    def parse_category(self, response):
	    items = response.xpath('//div[@class="box"]/table/tr')
	    for item in items:
	        print item.xpath('td[1]/a/text()').extract()[0] #link
	        print item.xpath('td[2]/text()').extract()[0]
	        print item.xpath('td[3]/text()').extract()[0]