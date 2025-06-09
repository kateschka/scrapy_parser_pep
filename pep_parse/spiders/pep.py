import scrapy

from pep_parse.items import PepParseItem

from pep_parse.settings import (
    ALLOWED_DOMAINS,
    SPIDER_NAME,
    START_URLS,
)


class PepSpider(scrapy.Spider):
    name = SPIDER_NAME
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URLS

    def parse(self, response):
        all_pep_links = response.css(
            'table.pep-zero-table tbody td a::attr(href)').getall()

        for link in all_pep_links:
            link = response.urljoin(link)
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        number = response.css(
            '#pep-content > h1::text').get().split(' – ')[0]
        name = response.css(
            '#pep-content > h1::text').get().split(' – ')[1]
        status = response.css('dt:contains("Status") + dd abbr::text').get()

        yield PepParseItem(number=number, name=name, status=status)
