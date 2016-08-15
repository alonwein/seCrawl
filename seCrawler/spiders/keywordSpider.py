__author__ = 'tixie'
from scrapy.selector import  Selector
from scrapy.spiders import Spider

from seCrawler.seCrawler import SearchEngineResultSelectors,SearchEngineTitleSelectors,SearchEngineUrlSelectors
from seCrawler.seCrawler import searResultPages


class keywordSpider(Spider):
    name = 'keywordSpider'
    allowed_domains = ['bing.com','google.com','baidu.com']
    start_urls = []
    keyword = None
    searchEngine = None
    selector = None


    def __init__(self, keyword, se = 'bing', pages = 50,  *args, **kwargs):
        super(keywordSpider, self).__init__(*args, **kwargs)
        self.keyword = keyword.lower()
        self.searchEngine = se.lower()
        self.selector = SearchEngineResultSelectors[self.searchEngine]
        pageUrls = searResultPages(keyword, se, int(pages))
        for url in pageUrls:
            print(url)
            self.start_urls.append(url)
        start_urls=self.start_urls
    def parse(self, response):
        for res in Selector(response).xpath(self.selector):
            title = ''.join(res.xpath(SearchEngineTitleSelectors[self.searchEngine]).extract())
            url = res.xpath(SearchEngineUrlSelectors[self.searchEngine]).extract()
            #for images- simply add the selector for the image and
            #image = res.xpath(SearchEngineImageSelectors[self.searchEngine]).extract()
            #image=''
            #if image:
                #image=imageManager.getImageBase64(image)
            #yield {'url': url,'title':title,'image':image}- will replace next
            yield {'url': url,'title':title}


