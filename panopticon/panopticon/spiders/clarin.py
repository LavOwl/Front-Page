from panopticon.spiders.doomscroller import DoomScroller
from datetime import datetime

class ClarinSpider(DoomScroller):
    name = "clarin"
    allowed_domains = ["clarin.com"]

    @property
    def start_urls(self):
        return ["https://www.clarin.com/politica/"]
    
    @property
    def forbidden_domains(self):
        return []

    @property
    def subdomains(self):
        return ["/politica/"]


    def parse_article(self, response):
        yield {
            "url": response.url,
            "title": response.css("h1::text").get(),
            "subtitle": response.css("h2.storySummary ul li::text").getall(),
            "author": response.css("div.author-info span::text").getall(),
            "tags": response.css("li.tag a::text").getall(),
            "date": self.parse_date(response),
            "body": self.parse_body(response),
            "diary": "Clarín"
        }

    #Falta implementar soporte para función "En Vivo"
    def parse_body(self, response):
        paragraphs = response.css("div#cuerpo div.container-text ::text").getall()
        return '\n'.join(paragraphs)

    def parse_date(self, response):
        try:
            raw_date = response.css("time.createDate::attr(datetime)").get()
            return datetime.fromisoformat(raw_date.replace("Z", "+00:00"))
        except Exception as e:
            return None
        