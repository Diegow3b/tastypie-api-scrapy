# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from twisted.internet import reactor
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from scrapy import log
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from crawler.spiders.letras_spider import LetrasSpider
from fabric.api import local

def stop_reactor():
    reactor.stop()

class Requisicao(models.Model):
    class Meta:
        verbose_name = u'Requisição'
        verbose_name_plural = u'Requisições'

    url = models.TextField()
    palavra = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    quantidade = models.IntegerField(null=True, blank=True)
    arquivo = models.CharField(max_length=100)

    @staticmethod
    def call_spider(key, url, json=None):        
        # Modo Simples
        local("scrapy crawl letras_spider -o {json} -t json -a url={url} -a key={key} -a json={json}".format(
            json = json if json else 'crawler_palavras.json',
            url = url,
            key = key
        ))
       
        # Modo Completo - Não está salvando em um arquivo Json
        # settings = get_project_settings()
        # settings.overrides['FEED_FORMAT'] = 'json'
        # settings.overrides['FEED_URI'] = 'result.json'
        # settings.overrides['ITEM_PIPELINES'] = {'__main__.JsonExportPipeline': 1}
        # configure_logging(settings=settings)
        # runner = CrawlerRunner(settings=get_project_settings())
        # d = runner.crawl('letras_spider', url=url, key=key)
        # d.addBoth(lambda _: reactor.stop())
        # reactor.run(installSignalHandlers=0)