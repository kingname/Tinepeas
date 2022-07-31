from tinepeas import Spider, Request


class ArchSpider(Spider):
    name = 'arch_spider'
    start_urls = []

    def start_requests(self):
        for page in range(1, 10):
            url = f'http://arch.kingname.info/html/news?page={page}'
            yield Request(url, callback=self.parse)

    def parse(self, response):
        news_list = response.xpath('//div[@class="news"]')
        for news in news_list:
            title = news.xpath('h3/a/text()').get(default='')
            content = news.xpath('div[@class="article"]/p/text()').getall()
            author = news.xpath('div[@class="author"]/text()').get()
            publish_time = news.xpath('div[@class="publish_ts"]/text()').get()
            print(f'{title} 【{author}】 {publish_time}')
            print(content)
