import wget
from scrapy import Spider, Item, Field, Request


class TheHyliaSpider(Spider):
	def __init__(self, category=None, *args, **kwargs):
		super(TheHyliaSpider, self).__init__(*args, **kwargs)
		self.start_urls = ['http://anime.thehylia.com/downloads/series/hunter-x-hunter-2011-']
		#self.lastpage = []
		
	name = 'the_hylia_spider'

	def parse(self, response):
		links = response.xpath('//td')
		for link in links:
			url = link.xpath('a[contains(@href, "download_file")]/@href')
			if len(url.extract()) > 0:
				#self.lastpage.append(url.extract()[0])
				yield Request(url.extract()[0], callback=self.download)
				#wget.download(url=url.extract()[0], out='/Users/trihatmaja/Download', bar=wget.bar_thermometer)
				#print url.extract()[0]
	def download(self, response):
		print response.url
		#wget.download(url=response.url, out='/Users/trihatmaja/Download')