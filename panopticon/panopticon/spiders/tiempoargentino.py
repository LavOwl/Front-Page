from panopticon.spiders.doomscroller import DoomScroller
from datetime import datetime
from typing import Generator, List
from scrapy.http import Response
from ..classes.article_dictionary import ArticleDict

class TiempoArgentinoSpider(DoomScroller):
    name: str = "tiempoargentino"
    allowed_domains: List[str] = ["tiempoar.com.ar"]
    start_urls: List[str] = ["https://www.tiempoar.com.ar"]

    @property
    def subdomains(self) -> List[str]:
        return ["/ta_article/"]
    
    @property
    def forbidden_domains(self) -> List[str]:
        return []

    def parse_article(self, response: Response) -> Generator[ArticleDict, None, None]:
        yield {
            "url": response.url,
            "title": response.css("h1::text").get(),
            "subtitle": response.css("div.subtitle h3::text").get(),
            "author": response.css("div.author-info p a::text").getall(),
            "date": self.parse_date(response),
            "body": self.parse_body(response),
            "tags": response.css("div.tag div.content a p::text").getall(),
            "newspaper": "Tiempo Argentino"
        }

    def parse_body(self, response: Response):
        content = response.xpath("//*[contains(@class, 'article-body')]//div//p | //div[contains(@class, 'article-body')]//div//h2")
        parts: List[str] = []
        for el in content:
            #tag = el.root.tag

            text = ' '.join(t.strip() for t in el.xpath(".//text()").getall() if t.strip())
            parts.append(text)
        
        return '\n'.join(parts)

    def parse_date(self, response: Response):
        raw_date: str | None = response.css("time::text").get()
        if raw_date:
            return datetime.strptime(raw_date + " 00:00", '%d/%m/%Y %H:%M')
        return datetime.now()