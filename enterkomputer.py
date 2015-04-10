from scrapy import Spider, Item, Field, Request

def complete_url(string):
    """Return complete url"""
    return "http://www.enterkomputer.com/" + string

class EnterkomputerSpider(Spider):
 
    name = 'enterkomputer_spider'
    start_urls = [
        'http://www.enterkomputer.com/sitemap.php'
    ]
 
    def parse(self, response):
        links = response.xpath('//li/a[contains(@href, ".php")]/@href').extract()
        for link in links:
            if (link not in ("sitemap.php", "about.php", "howto.php", "simulasi.php", "audio.php", "jne.php")):
                yield Request(complete_url(link), callback=self.parse_category)

    def parse_category(self, response):
        items = response.xpath('//tr')
        emptylist = []
        for item in items:
            product = item.xpath('td[2]/text()').extract()
            if(product != emptylist):
                print item.xpath('td[1]/text()').extract()[0].strip('[]')
                print product[0]