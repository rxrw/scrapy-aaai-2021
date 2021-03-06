# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AaaiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    track = scrapy.Field()
    title = scrapy.Field()
    abstract = scrapy.Field()
    names = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()

class PlenaryItem(scrapy.Item):
    title = scrapy.Field()
    pic_id = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
