__author__ = 'tixie'

SearchEngines = {
    'google': 'https://www.google.com/search?q={0}&start={1}',
    'bing': 'http://www.bing.com/search?q={0}&first={1}',
    'baidu': 'http://www.baidu.com/s?wd={0}&pn={1}'
}


SearchEngineResultSelectors= {
    'google': '//div/h3/',
    'bing':'//h2/a',
    'baidu':'//h3/a/',
}
SearchEngineTitleSelectors= {
    'bing':'node()',
    'baidu':'em.text()'
}
SearchEngineUrlSelectors= {
    'bing':'@href',
    'baidu':'@href'
}
SearchEngineImageSelectors= {
    #'bing':'//div[@class="rc"]',
    'baidu':'//h3/a/@href'
}