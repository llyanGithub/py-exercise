# -*- coding: utf-8 -*-
import scrapy
from baijia.items import AuthItem, ArticleItem
import pdb

class BaijiaSpiderSpider(scrapy.Spider):
    name = "baijia_spider"
    allowed_domains = ["baijia.baidu.com"]
    start_urls = (
        'http://baijia.baidu.com/?tn=listauthor',
    )

    def parse(self, response):
        authItem = AuthItem()
        for sel in response.xpath('//div[@class="authorlists"]/ul'):
#            pdb.set_trace()
            authItem['classification'] = sel.xpath('@data-name').extract()[0]
#            pdb.set_trace()
            if authItem['classification'] == u'\u516c\u53f8' or authItem['classification'] == u'\u5df2\u5173\u6ce8':
                continue
            for auth_sel in sel.xpath('li'):
                authItem['authName'] = auth_sel.xpath('div[@class="author-info"]/p[@class="userinf"]/a/text()').extract()[0]
                href = auth_sel.xpath('div[@class="author-info"]/p[@class="userinf"]/a/@href').extract()[0]
#                print authItem
                yield authItem
                
                url = response.urljoin(href)
                yield scrapy.Request(url, callback = self.parse_article)


    def parse_article(self, response):
        articleItem = ArticleItem()
        for sel in response.xpath('//div[@id="feeds"]/div'):
            articleItem['article_title'] = sel.xpath('h3/a/text()').extract()[0]
            articleItem['article_abstract'] = sel.xpath('p/text()').extract()[0]
            articleItem['article_href'] = sel.xpath('h3/a/@href').extract()[0]
            articleItem['auth_name'] = response.xpath('//div[@class="author-name"]/text()').extract()[0].replace('\n', '')
            articleItem['pic_href'] = '#'
            pic = sel.xpath('p[@class="feeds-item-pic"]/a/img/@src')
            if pic:
                articleItem['pic_href'] = pic.extract()[0]

            yield articleItem
