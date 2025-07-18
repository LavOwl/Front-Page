from panopticon.spiders.doomscroller import DoomScroller
from datetime import datetime
from typing import Generator, List
from scrapy.http import Response
from ..classes.article_dictionary import ArticleDict

class Pagina12Spider(DoomScroller):
    name: str = "pagina12"
    allowed_domains: List[str] = ["pagina12.com.ar"]
    start_urls:List[str] = ["https://www.pagina12.com.ar/secciones/el-pais", "https://www.pagina12.com.ar/secciones/economia"]

    @property
    def forbidden_domains(self) -> List[str]:
        return []

    @property
    def subdomains(self):
        return [("/" + str(i)) for i in range(10)]


    def parse_article(self, response: Response) -> Generator[ArticleDict, None, None]:
        yield {
            "url": response.url,
            "title": response.css("h1::text").get(),
            "subtitle": response.xpath('//h1/following-sibling::h2[1]/text()').get(),
            "author": response.css("div.author-name::text").getall(),
            "date": self.parse_date(response),
            "tags": [],
            "body": self.parse_body(response),
            "newspaper": "Página 12"
        }

    def parse_date(self, response: Response) -> datetime:
        date: str | None = response.css("time::attr(datetime)").get()
        if date:
            return datetime.fromisoformat(date)
        return datetime.now()

    def parse_body(self, response: Response) -> str:
        paragraphs: List[str] = []
        content = response.css("div.article-text")
        for child in content.xpath('./*'):
            text_nodes = child.xpath('.//text()').getall()
            cleaned = ' '.join(t.strip() for t in text_nodes if t.strip())
            if cleaned:
                paragraphs.append(cleaned)
        return '\n'.join(paragraphs)