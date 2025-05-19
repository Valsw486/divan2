import scrapy


class CsvSpider(scrapy.Spider):
    name = "csv"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://divan.ru"]

    def parse(self, response):
        pass
