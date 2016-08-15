import json

from klein import route, run

from seCrawler.spiders.seCarwler import seCrawler
from spiders.restSpider import  restSpider
from seCrawler.common.searResultPages import searResultPages

def return_spider_output(output):
    return json.dumps([dict(item) for item in output])


@route("/crawl")
def crawl(request):

    kwargs={}
    arg1=''
    if 'keyword' in request.args:
        kwargs['keyword']=request.args['keyword'][0]
        arg1='keyword='+request.args['keyword'][0]
    else:
        return "keyword is required"
    if 'pages' in request.args:
        pages=request.args['pages'][0]
        kwargs['pages'] = request.args['pages'][0]
        arg1 += 'pages=' + request.args['pages'][0]
    if 'se' in request.args:
        se=request.args['se'][0]
        #args['se'] = request.args['se'][0]
    runner = seCrawler()
    spider = restSpider(**kwargs)
    deferred = runner.crawl(spider,**kwargs)
    deferred.addCallback(return_spider_output)
    return deferred


run("localhost", 5000)