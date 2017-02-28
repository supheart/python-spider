# coding: utf-8

import loader
import MySQLdb
import urllib2
import time
import os

class MysqlSave(object):
    def __init__(self):
        self.conn = None
        self.loader = loader.Loader()

    def _conn (self):  
        try:  
            self.conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="testrelaxarticle", charset= "utf8")  
            return True  
        except :  
            return False

    def _reConn (self,num = 28800,stime = 3): #重试连接总次数为1天,这里根据实际情况自己设置,如果服务器宕机1天都没发现就......  
        _number = 0  
        _status = True  
        while _status and _number <= num:  
            try:  
                self.conn.ping()       #cping 校验连接是否异常  
                _status = False  
            except:  
                if self._conn() == True: #重新连接,成功退出  
                    _status = False  
                    break  
                _number +=1  
                time.sleep(stime)      #连接不成功,休眠3秒钟,继续循环，知道成功或重试次数结束 
    
    def _close(self):
        self.conn.close()

    def save(self, article, comments, imgList):
        try:
            self._reConn()

            self.insertArticle(article)
            self.insertHotComemts(comments)
            self.insertImage(imgList)
            # self.saveImgToDisk(imgList)
            # self.loader.loadImg(imgList)
            self.loader.loadImgWithFileStream(imgList)
        except Exception as e:
            raise(e)

    def insertArticle(self, article):
        self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)

        sqltext = u"insert into article (add_time, status, type, title, detailtime, imgsid, imgwh, hotComments, commCount, pubtime, mod_time, cover_img, content) values('%s','%s','%s','%s','%s','%s',%d,'%s','%s','%s','%s','%s','%s')" % (article['add_time'], article['status'], article['type'], article['title'], article['detailtime'], article['imgsid'], article['imgwh'], article['pkey'], article['commCount'], article['pubtime'], article['mod_time'], article['cover_img'], article['content'])
        # print(sqltext)
        rownum = self.cursor.execute(sqltext)

        self.conn.commit()
        self.cursor.close()
        return rownum

    def insertHotComemts(self, comments):
        self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)

        for comment in comments:
            commenttext = "insert into comment (avatar_sid, avatar_url, content, datetime, good, lou, `name`, `timestamp`, `user`, aid) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (comment['avatar_sid'], comment['avatar_url'], comment['content'], comment['datetime'], comment['good'], comment['lou'], comment['name'], comment['timestamp'], comment['user'], comment['aid'])
            print(commenttext)
            self.cursor.execute(commenttext)
        
        self.conn.commit()
        self.cursor.close()

    def insertImage(self, imgList):
        self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)

        # sourceimg.id,
        # sourceimg.aid,
        # sourceimg.img1,
        # sourceimg.img2,
        # sourceimg.img3,
        # sourceimg.img4,
        # sourceimg.img5,
        # sourceimg.img6,
        # sourceimg.img7,
        # sourceimg.img8,
        # sourceimg.img9,
        # sourceimg.img10
        imgs = imgList['imgList']
        img1 = imgs[0]['id'] + '.' + imgs[0]['extension']
        img2 = imgs[1]['id'] + '.' + imgs[1]['extension']
        img3 = imgs[2]['id'] + '.' + imgs[2]['extension']
        img4 = imgs[3]['id'] + '.' + imgs[3]['extension']
        img5 = imgs[4]['id'] + '.' + imgs[4]['extension']
        img6 = imgs[5]['id'] + '.' + imgs[5]['extension']
        img7 = imgs[6]['id'] + '.' + imgs[6]['extension']
        img8 = imgs[7]['id'] + '.' + imgs[7]['extension']
        img9 = imgs[8]['id'] + '.' + imgs[8]['extension']
        img10 = imgs[9]['id'] + '.' + imgs[9]['extension']
        rownum = self.cursor.execute("insert into sourceimg(aid, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (imgList['aid'],img1,img2,img3,img4,img5,img6,img7,img8,img9,img10))
        
        self.conn.commit()
        self.cursor.close()

    # def saveImgToDisk(self, imgList):
    #     for img in imgList['imgList']:
    #         try:
    #             imgUrl = 'http://iil.3b2o.com/img/show/sid/' + img['id'] + '/w/576/h/1000/t/0/show.' + img['extension']
    #             response = urllib2.urlopen(imgUrl)
    #             if response.getcode() != 200:
    #                 print(u'未下载成功：%s' % imgUrl)
    #                 continue
    #             filename = os.path.join(os.path.abspath('.'), "imgs", img['id'] + "." + img['extension'])
    #             with open(filename,'wb') as f:
    #                 f.write(response.read())
    #                 print(u'下载图片: %s' % imgUrl)
    #                 # time.sleep(0.05)
    #         except Exception as e:
    #             print(u'未下载成功：%s' % imgUrl)
    #             continue