import scrapy
from urllib.parse import urljoin
from abc import ABC, abstractmethod
from scrapy.http import Response
from typing import Generator, List
from ..classes.article_dictionary import ArticleDict

class DoomScroller(scrapy.Spider, ABC):
    
    @property
    @abstractmethod
    def subdomains(self) -> List[str]:
        pass

    @property
    @abstractmethod
    def forbidden_domains(self) -> List[str]:
        pass

    def parse(self, response: Response):
        base_url = "/".join(self.start_urls[0].split("/")[:3])
        links = response.css("a::attr(href)").getall()
        links = [link for link in links if link not in self.start_urls and link not in self.subdomains and link not in self.forbidden_domains]
        for link in links:
            for domain in self.subdomains:
                if link.startswith(base_url + domain):
                    yield scrapy.Request(link, callback=self.parse_article)

                elif link.startswith(domain):
                    link = urljoin(base_url, link)
                    yield scrapy.Request(link, callback=self.parse_article)
                    break

    @abstractmethod
    def parse_article(self, response: Response) -> Generator[ArticleDict, None, None]:
        pass