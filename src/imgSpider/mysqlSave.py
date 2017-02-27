# -*- coding: utf-8 -*-

import MySQLdb
import time

class MysqlSave(object):
    def __init__(self):
        self.conn = None

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
        except Exception as e:
            raise(e)

    def insertArticle(self, article):
        self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)

        # article.id,
        # article.add_time,
        # article.`status`,
        # article.type,
        # article.title,
        # article.detailtime,
        # article.imgsid,
        # article.imgwh,
        # article.hotComments,
        # article.commCount,
        # article.pubtime,
        # article.mod_time,
        # article.cover_img,
        # article.content
        # print(unicode(article['title'], 'gbk'))
        sqltext = "insert into article values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" % (article['add_time'], article['status'], article['type'], article['title'], article['detailtime'], article['imgsid'], article['imgwh'], article['pkey'], article['commCount'], article['pubtime'], article['mod_time'], article['cover_img'])
        print(sqltext)
        rownum = self.cursor.execute("insert into article values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" % (article['add_time'], article['status'], article['type'], article['title'], article['detailtime'], article['imgsid'], article['imgwh'], article['pkey'], article['commCount'], article['pubtime'], article['mod_time'], article['cover_img'], article['content']))

        self.conn.commit()
        self.cursor.close()
        return rownum

    def insertHotComemts(self, comments):
        self.cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)

        # `comment`.id,
        # `comment`.avatar_sid,
        # `comment`.avatar_url,
        # `comment`.content,
        # `comment`.datetime,
        # `comment`.good,
        # `comment`.lou,
        # `comment`.`name`,
        # `comment`.`timestamp`,
        # `comment`.`user`,
        # `comment`.aid
        for comment in comments:
            self.cursor.execute("insert into article values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" % (comment['avatar_sid'], comment['avatar_url'], comment['content'], comment['datetime'], comment['good'], comment['lou'], comment['name'], comment['timestamp'], comment['user'], comment['aid']))
        
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
        rownum = self.cursor.execute("insert into article values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" % (imgList['aid'],imgList['imgList'][0],imgList['imgList'][1],imgList['imgList'][2],imgList['imgList'][3],imgList['imgList'][4],imgList['imgList'][5],imgList['imgList'][6],imgList['imgList'][7],imgList['imgList'][8],imgList['imgList'][9]))
        
        self.conn.commit()
        self.cursor.close()
