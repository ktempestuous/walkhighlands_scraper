# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WalkhighlandsScraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    url = scrapy.Field()
    terrain = scrapy.Field()
    grade = scrapy.Field()
    bog = scrapy.Field()
    pass
