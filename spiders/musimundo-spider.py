import scrapy

class MusimundoSpider(scrapy.Spider):
    name = "musimundo"

    def start_requests(self):
        urls = [
            "https://www.musimundo.com/informatica/notebook/c/98"
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'musimundo-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Archivo creado: {filename}')

