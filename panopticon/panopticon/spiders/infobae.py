from panopticon.spiders.doomscroller import DoomScroller
from datetime import datetime

spanish_months = {
    'ene': '01', 'feb': '02', 'mar': '03', 'abr': '04',
    'may': '05', 'jun': '06', 'jul': '07', 'ago': '08',
    'sep': '09', 'oct': '10', 'nov': '11', 'dic': '12'
}

class InfobaeSpider(DoomScroller):
    name = "infobae"
    allowed_domains = ["infobae.com"]

    @property
    def start_urls(self):
        return ["https://infobae.com"]

    @property
    def subdomains(self):
        return ["/politica/"]
    
    @property
    def forbidden_domains(self):
        return []

    def parse_article(self, response):
        yield {
            "url": response.url,
            "title": response.css("h1::text").get(),
            "subtitle": response.css("h2.article-subheadline ::text"),
            "author": response.css("a.author-name::text").getall(),
            "date": self.parse_date(response),
            "body": self.parse_body(response),
            "tags": response.css("a.article-tag::text").getall(),
            "diary": "Infobae"
        }

    def parse_body(self, response):
        paragraphs = []
        for paragraph in response.css("p.paragraph"):
            paragraphs.append(" ".join(paragraph.xpath(".//text()").getall()))
        return '\n'.join(paragraphs)
    
    def parse_date(self, response):
        raw_text = response.css("span.sharebar-article-date::text").get().lower().replace('a.m.', 'AM').replace('p.m.', 'PM')

        day, month_name, year, time, am_pm = raw_text.replace(', ', ' ').split(' ')
        month = spanish_months[month_name.strip()]
        normalized = f'{day.zfill(2)}/{month}/{year} {time} {am_pm}'

        return datetime.strptime(normalized, "%d/%m/%Y %I:%M %p")
