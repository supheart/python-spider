# -*- coding: utf-8 -*
import urllib2
import urllib
import cookielib
import json

url = "http://www.baidu.com"
url_json = "http://zhiboba.3b2o.com/article/showListJson/EKo5qjn6Mq4"

# print urllib2.urlopen("http://baike.baidu.com/view/20965.htm").read()

readText = urllib2.urlopen(url_json).read()
content = json.loads(readText);
print content

urllib.urlretrieve("http://iil.3b2o.com/img/show/sid/pB_mREre1QT/w/576/h/1000/t/0/show.jpg", 'test.jpg')

print "第一种方法"
response1 = urllib2.urlopen(url)
print response1.getcode()
print len(response1.read())

print "第二种方法"
request = urllib2.Request(url)
request.add_header("user-agent", "Mozilla/5.0")
response2 = urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())

print "第三种方法"
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print response3.getcode()
print cj
print response3.read()

print ('end')
