# coding:utf8

class UrlManager(object):
    def __init__(self):
        self.newUrls = set()
        self.oldUrls = set()
    
    # 添加新的url到列表中
    def addUrl(self, url):
        if url is None:
            return
        # 新添加的url必须不在旧的url列表中
        if url not in self.newUrls and url not in self.oldUrls:
            self.newUrls.add(url)

    # 批量添加新的url
    def addUrls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.addUrl(url)

    # 判断是否存在新的url
    def hasUrl(self):
        return len(self.newUrls) != 0
    
    # 获取新的url内容
    def getUrl(self):
        newUrl = self.newUrls.pop()
        self.oldUrls.add(newUrl)
        return newUrl