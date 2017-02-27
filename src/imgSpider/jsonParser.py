# -*- coding: utf-8 -*-

import json
import shortuuid

class JsonParser(object):
    def _getArticle(self, content):
        return {
            'add_time': content['add_time'],
            'status': content['status'],
            'type': content['type'],
            'title': content['title'],
            'detailtime': content['detailtime'],
            'imgsid': content['imgsid'],
            'imgwh': content['imgwh'],
            'pkey': shortuuid.uuid(),
            'commCount': content['commCount'],
            'pubtime': content['pubtime'],
            'mod_time': content['mod_time'],
            'cover_img': content['cover_img'],
            'content': content['content']
        }

    def _getHotComment(self, content, pkey):
        if len(content['hotComments']) <= 0:
            return None
        models = []
        for comment in content['hotComments']:
            models.append({
                'avatar_sid': comment['avatar_sid'],
                'avatar_url': comment['avatar_url'],
                'content': comment['content'],
                'datetime': comment['datetime'],
                'good': comment['good'],
                'lou': comment['lou'],
                'name': comment['name'],
                'timestamp': comment['timestamp'],
                'user': comment['user'],
                'aid': pkey
            })
        return models

    def _getUrlsList(self, content, pkey):
        if len(content['contentJson']) <= 0:
            return None
        articleModels = set()
        imgModels = set()
        for urlObj in content['contentJson']:
            if urlObj['type'] == 'img':
                host = 'http://iil.3b2o.com/img/show/sid/' + urlObj['sid'] + '/w/576/h/1000/t/0/show.' + urlObj['extension']
                imgModels.add(host)
            elif urlObj['type'] == 'article':
                host = 'http://zhiboba.3b2o.com/article/showListJson/' + urlObj['sid']
                articleModels.add(host)

        return articleModels, {'imgList': imgModels, 'aid': pkey}
    
    def parse(self, url, content):
        if url is None or content is None:
            return
        try:
            jsonContent = json.loads(content)
            print(jsonContent['title'].encode("gbk"))
            # jsonContent['title'] = jsonContent['title'].encode("gbk")
            # jsonContent['content'] = jsonContent['content'].encode("gbk")
            article = self._getArticle(jsonContent)
            hotComment = self._getHotComment(jsonContent, article['pkey'])
            articleUrlList, imgUrlList = self._getUrlsList(jsonContent,  article['pkey'])
            return articleUrlList, article, hotComment, imgUrlList
        except Exception as e:
            raise(e)