from panopticon.spiders.doomscroller import DoomScroller
from datetime import datetime
from typing import Generator, List
from scrapy.http import Response
from ..classes.article_dictionary import ArticleDict

spanish_months = {
    'enero': '01', 'febrero': '02', 'marzo': '03', 'abril': '04',
    'mayo': '05', 'junio': '06', 'julio': '07', 'agosto': '08',
    'septiembre': '09', 'octubre': '10', 'noviembre': '11', 'diciembre': '12'
}


class LaNacionSpider(DoomScroller):
    name: str = "lanacion"
    allowed_domains: List[str] = ["lanacion.com.ar"]
    start_urls: List[str] = ["https://www.lanacion.com.ar/politica/"]

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
            "subtitle": response.css("h2.com-subhead ::text").get(),
            "author": list(dict.fromkeys(response.xpath("//a[contains(@href, 'autor')]//text()").getall())),
            "body": self.parse_body(response),
            "date": self.parse_date(response),
            "tags": response.xpath("//a[contains(@href, '/tema/')]//text()").getall(),
            "newspaper": "La Nación"
        }

    def parse_body(self, response: Response):
        content = response.xpath(
            "//p[contains(@class, 'com-paragraph')] | "
            "//h2[contains(@class, 'com-title')]"
        )

        parts: List[str] = []
        for el in content:
            #tag = el.root.tag

            text = ' '.join(t.strip() for t in el.xpath(".//text()").getall() if t.strip())
            parts.append(text)

        return '\n'.join(parts)

    def parse_date(self, response: Response):
        date, time = response.css("time::text").getall()

        day, month_name, year = date.split(' de ')
        month = spanish_months[month_name.strip()]
        normalized_string = f'{day.zfill(2)}/{month}/{year.strip()} {time}'

        return datetime.strptime(normalized_string, '%d/%m/%Y %H:%M')