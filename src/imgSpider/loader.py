# coding: utf-8

import urllib2
import urllib
import os

class Loader(object):
    def download(self, url):
        if(url is None):
            return None

        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None

        return response.read()
    
    def loadImgWithFileStream(self, imgList):
        for img in imgList['imgList']:
            try:
                imgUrl = 'http://iil.3b2o.com/img/show/sid/' + img['id'] + '/w/576/h/1000/t/0/show.' + img['extension']
                response = urllib2.urlopen(imgUrl)
                if response.getcode() != 200:
                    print(u'未下载成功：%s' % imgUrl)
                    continue
                filename = os.path.join(os.path.abspath('.'), "imgs", img['id'] + "." + img['extension'])
                with open(filename,'wb') as f:
                    f.write(response.read())
                    print(u'下载图片: %s' % imgUrl)
                    # time.sleep(0.05)
            except Exception as e:
                print(u'未下载成功：%s' % imgUrl)
                continue

    def loadImg(self, imgList):
        for img in imgList['imgList']:
            try:
                imgUrl = 'http://iil.3b2o.com/img/show/sid/' + img['id'] + '/w/576/h/1000/t/0/show.' + img['extension']
                filename = os.path.join(os.path.abspath('.'), "imgs", img['id'] + "." + img['extension'])
                urllib.URLopener.version = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0'
                #下载图片到指定目录中，保留图片在服务器上的文件名
                urllib.urlretrieve(imgUrl, filename)
                print(u'下载图片: %s' % imgUrl)
                    # time.sleep(0.05)
            except Exception as e:
                print(u'未下载成功：%s' % imgUrl)
                continue 
    
