from panopticon.spiders.doomscroller import DoomScroller
from datetime import datetime

class TiempoArgentinoSpider(DoomScroller):
    name = "tiempoargentino"
    allowed_domains = ["tiempoar.com.ar"]
   
   
    @property
    def start_urls(self):
        return ["https://www.tiempoar.com.ar"]

    @property
    def subdomains(self):
        return ["/ta_article/"]
    
    @property
    def forbidden_domains(self):
        return []

    def parse_article(self, response):
        yield {
            "url": response.url,
            "title": response.css("h1::text").get(),
            "subtitle": response.css("div.subtitle h3::text").get(),
            "author": response.css("div.author-info p a::text").getall(),
            "date": self.parse_date(response),
            "body": self.parse_body(response),
            "tags": response.css("div.tag div.content a p::text").getall(),
            "diary": "Tiempo Argentino"
        }

    def parse_body(self, response):
        content = response.xpath("//div[contains(@class, 'art-column-w-lpadding')]//p | //div[contains(@class, 'art-column-w-lpadding')]//h2")
        parts = []
        for el in content:
            #tag = el.root.tag

            text = ' '.join(t.strip() for t in el.xpath(".//text()").getall() if t.strip())
            parts.append(text)
        
        return '\n'.join(parts)

    def parse_date(self, response):
        raw_date = response.css("time::text").get()
        return datetime.strptime(raw_date + " 00:00", '%d/%m/%Y %H:%M')