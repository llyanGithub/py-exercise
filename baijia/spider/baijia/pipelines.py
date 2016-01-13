# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
import os
import pdb

from baijia.items import AuthItem, ArticleItem

class BaijiaPipeline(object):
    def __init__(self):
#        self.dbName = '/Users/yanlinglong/scrapy_project/baijia/test.db'
        self.dbName = '/Users/yanlinglong/Tmp/django_sites/Baijia/db.sqlite3'
#        if os.path.exists(self.dbName):
#            os.remove(self.dbName)
        self.cx = sqlite3.connect(self.dbName)
        self.cu = self.cx.cursor()

#        self.cu.execute('create table auth_table("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "auth_name" varchar(20) NOT NULL, "classification" varchar(20) NOT NULL)')
#        self.cx.commit()

#        self.cu.execute('create table article_table("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "article_title" varchar(100) NOT NULL, "article_abstract" varchar(500) NOT NULL, "article_href" varchar(100) NOT NULL, "auth_id" integer NOT NULL REFERENCES “auth_table” ("id"))')
#        self.cx.commit()

    def process_item(self, item, spider):
        if isinstance(item, AuthItem):
            self.cu.execute('select auth_name from articles_author where auth_name="%s" and classification="%s"' % (item["authName"], item["classification"]))
            self.cx.commit()
            result = self.cu.fetchall()
            if result:
                return

            self.cu.execute('insert into articles_author(auth_name, classification) values("%s","%s")' % (item["authName"], item["classification"]))
            self.cx.commit()
        elif isinstance(item, ArticleItem):
            self.cu.execute('select id from articles_articles where article_title="%s"' % item["article_title"])
            self.cx.commit()
            result = self.cu.fetchall()
            if result:
                return

            self.cu.execute('select id from articles_author where auth_name="%s"' % item["auth_name"])
            self.cx.commit()

            result = self.cu.fetchall()
#            pdb.set_trace()
            auth_id = 0
            if result:
                auth_id = result[0][0]
                self.cu.execute('insert into articles_articles (article_title, article_abstract, article_href, auth_id_id, pic_href) values("%s", "%s", "%s", %d, "%s")' % (item["article_title"], item["article_abstract"], item['article_href'], auth_id, item['pic_href']))
                self.cx.commit()

    def __del__(self):
        self.cu.close()
        self.cx.close()
