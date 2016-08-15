from scrapy import signals
from scrapy.crawler import CrawlerRunner



class seCrawler(CrawlerRunner):
    def crawl(self, spider, *args, **kwargs):
        self.items = []

        crawler = self.create_crawler(spider)

        crawler.signals.connect(self.item_scraped, signals.item_scraped)

        dfd = self._crawl(crawler, *args, **kwargs)

        dfd.addCallback(self.return_items)
        return dfd

    def item_scraped(self, item, response, spider):
        self.items.append(item)

    def return_items(self, result):
        return self.items