# -*- coding: utf-8 -*-
import datetime
import socket
import scrapy

from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose

from snl.items import Draw


class Super6Spider(scrapy.Spider):
    name = 'super6'
    allowed_domains = ['stlucialotto.com']
    start_urls = ['http://www.stlucialotto.com/snl/super6.php']

    def parse(self, response):
        """
        This function parses the winning numbers page of SNL

        @url http://www.stlucialotto.com/snl/super6.php
        @returns items 1
        @scrapes draw_date first second third fourth fifth sixth letter
        @scrapes url project spider server date
        """
        d = ItemLoader(item=Draw(), response=response)
        d.add_xpath('draw_date',
        '//span[@class="header2"][2]/text()')
        d.add_xpath('first',
                '//*[@class="game_results_large s6_r"]/ul/li[1]/text()')
        d.add_xpath('second',
                '//*[@class="game_results_large s6_r"]/ul/li[2]/text()')
        d.add_xpath('third',
                '//*[@class="game_results_large s6_r"]/ul/li[3]/text()')
        d.add_xpath('fourth',
                '//*[@class="game_results_large s6_r"]/ul/li[4]/text()')
        d.add_xpath('fifth',
                '//*[@class="game_results_large s6_r"]/ul/li[5]/text()')
        d.add_xpath('sixth',
                '//*[@class="game_results_large s6_r"]/ul/li[6]/text()')
        d.add_xpath('letter',
                '//*[@class="game_results_large s6_r"]/ul/li[7]/text()',
                MapCompose(str.strip))
        d.add_value('url', response.url)
        d.add_value('project', self.settings.get('BOT_NAME'))
        d.add_value('spider', self.name)
        d.add_value('server', socket.gethostname())
        d.add_value('date', datetime.datetime.now())
        return d.load_item()

