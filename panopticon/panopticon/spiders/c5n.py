from panopticon.spiders.doomscroller import DoomScroller
from datetime import datetime
from scrapy.http import Response
from typing import Generator, List
from ..classes.article_dictionary import ArticleDict

class C5nSpider(DoomScroller):
    name: str = "c5n"
    allowed_domains: List[str] = ["c5n.com"]
    start_urls: List[str] = ["https://www.c5n.com/politica/"]


    @property
    def subdomains(self) -> List[str]:
        return ["/politica/"]
    
    @property
    def forbidden_domains(self) -> List[str]:
        return [("https://www.c5n.com/politica/" + str(i)) for i in range(10)]

    def parse_article(self, response: Response) -> Generator[ArticleDict, None, None]:
        yield {
            "url": response.url,
            "title": response.css("h1::text").get(),
            "subtitle": response.css("h2.news_headline__article-summary::text").get(),
            "author": response.css("span.news-headline__author-name a::text").getall(),
            "tags": response.css("li.news-topics__list-item a::text").getall(),
            "date": self.parse_date(response),
            "body": self.parse_body(response),
            "newspaper": "c5n"
        }

    def parse_date(self, response: Response) -> datetime:
        date:str | None = response.css("span.news-headline__date time::attr(datetime)").get()
        if date:
            date = date.replace('Z', '+00:00')
            return datetime.fromisoformat(date)
        return datetime.now()

    def parse_body(self, response: Response) -> str:
        paragraphs: List[str] = []
        for article in response.css('article'):
            if article.xpath('ancestor::a').get():
                continue

            for child in article.xpath('./*'):
                text_nodes = child.xpath('.//text()').getall()
                cleaned = ' '.join(t.strip() for t in text_nodes if t.strip())
                if cleaned:
                    paragraphs.append(cleaned)
        return '\n'.join(paragraphs)