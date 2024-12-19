import scrapy


class DocstatsSpider(scrapy.Spider):
    name = "docstats"
    allowed_domains = ["tradingeconomics.com"]
    start_urls = ["https://tradingeconomics.com/country-list/medical-doctors?continent=world"]

    def parse(self, response):
        medstats = response.xpath("//td/a")
        for medstat in medstats:
            country = medstat.xpath(".//text()").get()
            link = medstat.xpath(".//@href").get()
            yield{response.follow (url=link, callback=self.parse_docstat, meta = {"country":country})}
    def parse_docstat(self,response):
        rows = response.xpath("//tr[contains(@class,'datatable)]")
        for row in rows:
            related = row.xpath(".//td/a/text()").get().strip()
            last = float(row.xpath(".//td[2]/text()").get())
            previous = float(row.xpath(".//td[3]/text()").get())
            country = response.request.meta['country']
            yield{"country":country,
                  "related":related,
                  "last":last,
                  "previous":previous}
