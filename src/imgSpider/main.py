# coding: utf-8

import urlManager, loader, jsonParser, mysqlSave

class SpiderMain(object):
    # 初始化对象
    def __init__(self):
        self.urls = urlManager.UrlManager()
        self.loader = loader.Loader()
        self.parser = jsonParser.JsonParser()
        self.saver = mysqlSave.MysqlSave()

    def craw(self, rootUrl):
        count = 1
        print('start craw img...')
        self.urls.addUrl(rootUrl)
        # 遍历数组，解析每个url的内容
        while self.urls.hasUrl():
            try:
                newUrl = self.urls.getUrl()
                print('craw %d : %s' % (count, newUrl))
                content = self.loader.download(newUrl)
                newUrls, article, hotComment, imgList = self.parser.parse(newUrl, content)
                self.urls.addUrls(newUrls)
                self.saver.save(article, hotComment, imgList)

                if count == 30:
                    break
                count = count + 1
            except Exception as e:
                print('craw failed ' + str(e))

        # self.outputer.output_html()

if __name__=="__main__":
    # 定义网址趴取的入口
    rootUrl = "http://zhiboba.3b2o.com/article/showListJson/ppdhREre1QG"
    objSpider = SpiderMain()
    objSpider.craw(rootUrl)