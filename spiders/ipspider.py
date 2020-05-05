from tinepeas import Spider, Request


class IpSpider(Spider):
    name = 'ipspider'
    start_urls = []

    def start_requests(self):
        for page in range(1, 1000):
            url = f'http://exercise.kingname.info/exercise_middleware_ip/{page}'
            yield Request(url, callback=self.parse)

    def parse(self, response):
        print(response.body)
