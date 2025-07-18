from panopticon.spiders.doomscroller import DoomScroller
from datetime import datetime

class Pagina12Spider(DoomScroller):
    name = "pagina12"
    allowed_domains = ["pagina12.com.ar"]

    @property
    def forbidden_domains(self):
        return []

    @property
    def start_urls(self):
        return ["https://www.pagina12.com.ar/secciones/el-pais", "https://www.pagina12.com.ar/secciones/economia"]

    @property
    def subdomains(self):
        return [("/" + str(i)) for i in range(10)]


    def parse_article(self, response):
        yield {
            "url": response.url,
            "title": response.css("h1::text").get(),
            "subtitle": response.xpath('//h1/following-sibling::h2[1]/text()').get(),
            "author": response.css("div.author-name::text").getall(),
            "date": datetime.fromisoformat(response.css("time::attr(datetime)").get()),
            "body": self.parse_body(response),
            "diary": "Página 12"
        }

    def parse_body(self, response):
        paragraphs = []
        content = response.css("div.article-text")
        for child in content.xpath('./*'):
            text_nodes = child.xpath('.//text()').getall()
            cleaned = ' '.join(t.strip() for t in text_nodes if t.strip())
            if cleaned:
                paragraphs.append(cleaned)
        return '\n'.join(paragraphs)