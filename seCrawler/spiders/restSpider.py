from scrapy.selector import Selector
from scrapy.spiders import Spider
from seCrawler.common.searchEngines import SearchEngineResultSelectors,SearchEngineTitleSelectors,SearchEngineUrlSelectors
from seCrawler.common.searResultPages import searResultPages
from seCrawler.common.imageManager import imageManager

class restSpider(Spider):
    name = 'restSpider'
    allowed_domains = ['bing.com','google.com','baidu.com']
    start_urls = []
    keyword = None
    searchEngine = None
    selector = None


    def __init__(self, keyword, se = 'bing', pages = 50,  *args, **kwargs):
        super(restSpider, self).__init__(*args, **kwargs)
        self.keyword = keyword.lower()
        self.searchEngine = se.lower()
        self.selector = SearchEngineResultSelectors[self.searchEngine]
        pageUrls = searResultPages(keyword, se, int(pages))
        for url in pageUrls:
            print(url)
            self.start_urls.append(url)
        start_urls=self.start_urls
    def parse(self, response):
        sites = []
        for res in Selector(response).xpath(self.selector):
            site = {}
            title = ''.join(res.xpath(SearchEngineTitleSelectors[self.searchEngine]).extract())
            url = res.xpath(SearchEngineUrlSelectors[self.searchEngine]).extract()
            #for images- simply add the selector for the image and
            #image = res.xpath(SearchEngineImageSelectors[self.searchEngine]).extract()
            #image=''
            #if image:
                #image=imageManager.getImageBase64(image)
            #yield {'url': url,'title':title,'image':image}- will replace next
            try:
                site['url']=url
                site['title'] = title
            except Exception as e:
                print e
            #yield site
            sites.append(site)
        return sites
