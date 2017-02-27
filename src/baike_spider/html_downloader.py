# coding:utf8

# from urllib import request
import urllib2

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
            
        # response = request.urlopen(url)
        response = urllib2.urlopen(url)
        if(response.getcode() != 200):
            return None

        return response.read()