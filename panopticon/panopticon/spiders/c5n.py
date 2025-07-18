from panopticon.spiders.doomscroller import DoomScroller
from datetime import datetime

class C5nSpider(DoomScroller):
    name = "c5n"
    allowed_domains = ["c5n.com"]

    @property
    def start_urls(self):
        return ["https://www.c5n.com/politica/"]

    @property
    def subdomains(self):
        return ["/politica/"]
    
    @property
    def forbidden_domains(self):
        return [("https://www.c5n.com/politica/" + str(i)) for i in range(10)]

    def parse_article(self, response):
        yield {
            "url": response.url,
            "title": response.css("h1::text").get(),
            "subtitle": response.css("h2.news_headline__article-summary::text").get(),
            "author": response.css("span.news-headline__author-name a::text").getall(),
            "tags": response.css("li.news-topics__list-item a::text").getall(),
            "date": datetime.fromisoformat(response.css("span.news-headline__date time::attr(datetime)").get().replace('Z', '+00:00')),
            "body": self.parse_body(response),
            "diary": "c5n"
        }

    def parse_body(self, response):
        paragraphs = []
        for article in response.css('article'):
            if article.xpath('ancestor::a').get():
                continue

            for child in article.xpath('./*'):
                text_nodes = child.xpath('.//text()').getall()
                cleaned = ' '.join(t.strip() for t in text_nodes if t.strip())
                if cleaned:
                    paragraphs.append(cleaned)
        return '\n'.join(paragraphs)