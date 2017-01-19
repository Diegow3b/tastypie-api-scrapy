# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
import scrapy, re, json, tempfile, os
from datetime import datetime
from fabric.api import local
from os.path import exists

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

class LetrasSpider(scrapy.Spider):
    name = "letras_spider"
    allowed_domains = []
    start_urls = ('',)
    key = ''
    json = ''

    def __init__(self, category=None, *args, **kwargs):
        super(LetrasSpider, self).__init__(*args, **kwargs)
        url = kwargs.get("url")
        key = kwargs.get("key")
        self.json = kwargs.get("json") if kwargs.get("json") else ''
        if url and key:
            if not url.startswith('http://') and not url.startswith('https://'):
                url = 'http://%s/' % url
            self.allowed_domains = [url,]
            self.start_urls = [url,]
            self.key = key
        else:
            raise ValidationError(u'Parametros não foram passados corretamente - key: {key} - url: {url}'.format(key=kwargs.get("key"), url=kwargs.get("url")))

    def parse(self, response, **kwargs):
        word = self.key
        page_cleaned = cleanhtml(response.body)        
        words = re.findall(r'(?:^|\W){word}(?:$|\W)'.format(word=word), page_cleaned)
        yield {
            "palavra": self.key,
            "url" : self.url,
            "quantidade" : len(words),
            "data" : datetime.now(),
            "arquivo": self.json,
            }

    def closed(self, reason, **kwargs):
        pass
        # if exists(self.json):
        #     # with open(self.json) as data_file:
        #     with open(self.json) as data_file:
        #         data = data_file.read()
        #         json_file = json.loads(json.dumps(data))
        #         body_json = {
        #             "model": "requisicao.requisicao",
        #             "fields": {
        #             }
        #         }
        #         # ...
        #         local("./manage.py loaddata {json}".format(self.json))