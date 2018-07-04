# -*- coding: utf-8 -*-

from scrapy.item import Item, Field


class Draw(Item):

    draw_date = Field()
    first = Field()
    second = Field()
    third = Field()
    fourth = Field()
    fifth = Field()
    sixth = Field()
    letter = Field()

    # Housekeeping
    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()


