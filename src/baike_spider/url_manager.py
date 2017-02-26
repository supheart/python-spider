# coding:utf8

# url管理器
class UrlManager(object):
    # 构造函数初始化两个数组
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
        
    # 添加新的url到列表中
    def add_new_url(self, url):
        if url is None:
            return
        # 新添加的url必须不在旧的url列表中
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    # 批量添加新的url
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    # 判断是否存在新的url
    def has_new_url(self):
        return len(self.new_urls) != 0
    
    # 获取新的url内容
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
        