from scrapy import Spider, Item, Field, Request, FormRequest

def complete_url(string):
    """Return complete url"""
    return "http://www.waroengkom.com/" + string

class WaroengkomSpider(Spider):
 
    name = 'waroengkom_spider'
    start_urls = [
        'http://www.waroengkom.com/'
    ]
 
    def parse(self, response):
        links = response.xpath('//div[@id="content"]//li/a/@href').extract()
        for link in links:
            yield Request(complete_url(link), callback=self.parse_category)

    def parse_category(self, response):
        items = response.xpath('//div[@class="datagrid"]//tr')
        for item in items:
            product = item.xpath('td//font/b/span[contains(@id, "main_GDVMain_lblProductName")]/text()').extract()
            #price = item.xpath('td//font/b/span[contains(@id, "main_GDVMain_lblHarga")]/text()').extract()
            #link = 
            if (len(product) > 0):
                print product
                
            pages = item.xpath('td[@colspan="3"]//a/@href').re("doPostBack\(([^)]+')")
            if len(pages) > 0:
                for page in pages:
                    yield FormRequest.from_response(response, formdata={'__EVENTTARGET': eventtarget, '__EVENTARGUMENT': eventargument}, callback = self.parse_items, dont_click = True)

    def parse_items(self, response):
        items = response.xpath('//div[@class="datagrid"]//tr')
        for item in items:
            product = item.xpath('td//font/b/span[contains(@id, "main_GDVMain_lblProductName")]/text()').extract()
            #price = item.xpath('td//font/b/span[contains(@id, "main_GDVMain_lblHarga")]/text()').extract()
            if(len(product) > 0):
                print product
        