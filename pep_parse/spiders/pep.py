import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

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
