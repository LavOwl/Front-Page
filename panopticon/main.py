from datetime import datetime, timedelta, time
import time as time_module
import pytz

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from panopticon.spiders import lanacion, clarin, c5n, eldestape, infobae, pagina12, tiempoargentino

TIMEZONE = pytz.timezone("America/Argentina/Buenos_Aires")
SPIDERS = [
    lanacion.LaNacionSpider,
    clarin.ClarinSpider,
    c5n.C5nSpider,
    eldestape.EldestapeSpider,
    infobae.InfobaeSpider,
    pagina12.Pagina12Spider,
    tiempoargentino.TiempoArgentinoSpider,
]

def run_spiders():
    process = CrawlerProcess(get_project_settings())
    for spider in SPIDERS:
        process.crawl(spider)
    process.start()

def main():
    now = datetime.now(TIMEZONE)
    target_time = TIMEZONE.localize(datetime.combine(now.date(), time(0, 0)))

    if now > target_time:
        run_spiders()

    while True:
        now = datetime.now(TIMEZONE)
        sleep_seconds = (target_time - now).total_seconds()
        if sleep_seconds < 0:
            sleep_seconds += 86400  # Wait for next day's 8am
            target_time = target_time + timedelta(days=1)
        time_module.sleep(sleep_seconds)
        run_spiders()

if __name__ == "__main__":
    main()