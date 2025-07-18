from panopticon.spiders.doomscroller import DoomScroller
from datetime import datetime
from typing import Generator, List
from scrapy.http import Response
from ..classes.article_dictionary import ArticleDict

spanish_months = {
    'ene': '01', 'feb': '02', 'mar': '03', 'abr': '04',
    'may': '05', 'jun': '06', 'jul': '07', 'ago': '08',
    'sep': '09', 'oct': '10', 'nov': '11', 'dic': '12'
}

class InfobaeSpider(DoomScroller):
    name:str = "infobae"
    allowed_domains: List[str] = ["infobae.com"]
    start_urls: List[str] = ["https://infobae.com"]

    @property
    def subdomains(self):
        return ["/politica/"]
    
    @property
    def forbidden_domains(self) -> List[str]:
        return []

    def parse_article(self, response: Response) -> Generator[ArticleDict, None, None]:
        yield {
            "url": response.url,
            "title": response.css("h1::text").get(),
            "subtitle": response.css("h2.article-subheadline::text").get(),
            "author": response.css("a.author-name::text").getall(),
            "date": self.parse_date(response),
            "body": self.parse_body(response),
            "tags": response.css("a.article-tag::text").getall(),
            "newspaper": "Infobae"
        }

    def parse_body(self, response:Response) -> str:
        paragraphs: List[str] = []
        for paragraph in response.css("p.paragraph"):
            paragraphs.append(" ".join(paragraph.xpath(".//text()").getall()))
        return '\n'.join(paragraphs)
    
    def parse_date(self, response: Response):
        raw_text: str | None = response.css("span.sharebar-article-date::text").get()
        if raw_text:
            raw_text = raw_text.lower().replace('a.m.', 'AM').replace('p.m.', 'PM')

            for suffix in [' AM', ' PM']:
                if suffix in raw_text:
                    raw_text = raw_text.split(suffix)[0] + suffix
                    break

            day, month_name, year, time, am_pm = raw_text.replace(', ', ' ').split(' ')
            month = spanish_months[month_name.strip()]
            normalized = f'{day.zfill(2)}/{month}/{year} {time} {am_pm}'

            return datetime.strptime(normalized, "%d/%m/%Y %I:%M %p")
        return datetime.now()
