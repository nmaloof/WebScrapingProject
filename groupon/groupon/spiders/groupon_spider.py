from scrapy import Spider, Request
from groupon.items import GrouponItem

class GrouponSpider(Spider):
	name = "groupon_spider"
	allowed_urls = ['https://groupon.com']
	start_urls = ['https://www.groupon.com/browse/new-york?context=local&page=' + str(i) for i in range(1,17)]
	#start_urls = ['https://www.groupon.com/browse/new-york?context=local&page=1']

	def parse(self, response):
		try:
			url_list = response.xpath('//figure/a/@href').extract()
			for url in url_list:
				yield Request(url, callback = self.parse_links, meta = {'state':'New York', 'url': url})
		except:
			pass

	def parse_links(self, response):
		try:
			promotion_title = response.xpath('//h1[@class="deal-page-title small-title"]/text()').extract_first().strip()

			merchant = response.xpath('//div[@id="deal-subtitle-container"]/h2/span/span/text()').extract_first()

			rel_location = response.xpath('//a[@class="merchant-info-anchor"]/text()').extract_first().strip()

			total_ratings = response.xpath('//h3[@class="ugc-star-ratings"]/a[@href="#tips"]/span/text()').extract_first()

			deal_features = response.xpath('//div[@itemprop="description"]//text()').extract()
			deal_features = [x.strip() for x in deal_features if x != '\n']
			deal_features = [x for x in deal_features if x not in ['.', '']]

			mini_info = response.xpath('//div[@id="purchase-cluster"]//div[@class="text"]/text()').extract()
			mini_info = [x.strip() for x in mini_info]

			categories = response.xpath('//div[@class="columns"]//text()').extract()
			categories = [y for y in [x.strip() for x in categories] if y not in['','›']]

			item = GrouponItem()
			item['promotion_title'] = promotion_title
			item['merchant'] = merchant
			item['rel_location'] = rel_location
			item['total_ratings'] = total_ratings
			item['deal_features'] = deal_features
			item['mini_info'] = mini_info
			item['state'] = response.meta['state']
			item['categories'] = categories
			item['url'] = response.meta['url']

			yield item

		except:
			pass