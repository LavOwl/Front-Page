from panopticon.spiders.doomscroller import DoomScroller
from datetime import datetime

spanish_months = {
    'enero': '01', 'febrero': '02', 'marzo': '03', 'abril': '04',
    'mayo': '05', 'junio': '06', 'julio': '07', 'agosto': '08',
    'septiembre': '09', 'octubre': '10', 'noviembre': '11', 'diciembre': '12'
}

class EldestapeSpider(DoomScroller):
    name = "eldestape"
    allowed_domains = ["eldestapeweb.com"]

    @property
    def start_urls(self):
        return ["https://www.eldestapeweb.com"]

    @property
    def subdomains(self):
        return ["/politica/"]
    
    @property
    def forbidden_domains(self):
        return []


    def parse_article(self, response):
        yield {
            "url": response.url,
            "title": response.css("h1::text").get(),
            "subtitle": response.css("h2.intro ::text").get(),
            "author": response.css("p.firmante a::text").getall(),
            "date": self.parse_date(response),
            "body": self.parse_body(response),
            "tags": response.css("ul.palabras li a::text").getall(),
            "diary": "El Destape"
        }

    def parse_body(self, response):
        content = response.css("div.cuerpo p")
        paragraphs = []
        for paragraph in content:
            paragraphs.append(' '.join(t.strip() for t in paragraph.xpath(".//text()").getall() if t.strip()))
        return '\n'.join(paragraphs)

    def parse_date(self, response):
        date_text = response.css('div.fecha span::text').get().lower()
        time_text = response.css('div.fecha span.hora::text').get().strip(' | ').replace('.', ':')
        day, month_name, year = date_text.replace(',', ' de ').split(' de ')
        month = spanish_months[month_name.strip()]
        normalized_string = f'{day.zfill(2)}/{month}/{year.strip()} {time_text}'

        return datetime.strptime(normalized_string, '%d/%m/%Y %H:%M')