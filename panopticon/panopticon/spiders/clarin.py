from panopticon.spiders.doomscroller import DoomScroller
from datetime import datetime
from scrapy.http import Response
from ..classes.article_dictionary import ArticleDict
from typing import Generator, List

class ClarinSpider(DoomScroller):
    name: str = "clarin"
    allowed_domains: List[str] = ["clarin.com"]
    start_urls: List[str] = ["https://www.clarin.com/politica/"]
    
    @property
    def forbidden_domains(self) -> List[str]:
        return []

    @property
    def subdomains(self):
        return ["/politica/"]


    def parse_article(self, response: Response) -> Generator[ArticleDict, None, None]:
        yield {
            "url": response.url,
            "title": response.css("h1::text").get(),
            "subtitle": response.css("h2.storySummary ul li::text").get(),
            "author": response.css("div.author-info span::text").getall(),
            "tags": response.css("li.tag a::text").getall(),
            "date": self.parse_date(response),
            "body": self.parse_body(response),
            "newspaper": "Clarín"
        }

    #Falta implementar soporte para función "En Vivo"
    def parse_body(self, response: Response) -> str:
        paragraphs = response.css("div#cuerpo div.container-text ::text").getall()
        return '\n'.join(paragraphs)

    def parse_date(self, response: Response) -> datetime:
        raw_date: str | None = response.css("time.createDate::attr(datetime)").get()
        if raw_date:
            return datetime.fromisoformat(raw_date.replace("Z", "+00:00"))
        return datetime.now()
        