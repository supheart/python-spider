# coding:utf8

import urlManager, loader, parse

class SpiderMain(object):
    # 初始化对象
    def __init__(self):
        self.urls = urlManager.UrlManager()
        self.loader = loader.Loader()
        self.parser = parse.Parser()

    def craw(self, rootUrl):
        count = 1
        print('start craw img...')
        self.urls.addUrl(rootUrl)
        # 遍历数组，解析每个url的内容
        while self.urls.hasUrl():
            try:
                # new_url = self.urls.get_new_url()
                # print('craw %d : %s' % (count, new_url))
                # html_content = self.downloader.download(new_url)
                # new_urls, new_data = self.parser.parse(new_url, html_content)
                # self.urls.add_new_urls(new_urls)
                # self.outputer.collect_data(new_data)

                if count == 30:
                    break
                count = count + 1
            except Exception as e:
                print('craw failed' + str(e))

        # self.outputer.output_html()

if __name__=="__main__":
    # 定义网址趴取的入口
    rootUrl = "http://baike.baidu.com/item/Python"
    objSpider = SpiderMain()
    objSpider.craw(rootUrl)