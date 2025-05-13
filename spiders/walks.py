import scrapy
import os

class WalkhighlandsSpider(scrapy.Spider):
    name = "walks"
    allowed_domains = ["walkhighlands.co.uk"]
    start_urls = ["https://www.walkhighlands.co.uk"]

    def __init__(self, *args, **kwargs): # delete output file if it exists already
        super().__init__(*args, **kwargs)
        self.output_file = "walks.json"
        if os.path.exists(self.output_file):
            os.remove(self.output_file)
            self.log(f"Deleted previous output file: {self.output_file}")
        self.data = []

    def parse(self, response):
        # Collect URLS for regions to then look into
        region_links = response.css("table.table1.table2 tbody tr td a::attr(href)").getall()
        print(region_links)
        for region_link in region_links:
             print("Going through hikes in region: ,", region_link)
             yield response.follow(region_link, callback=self.parse_region)

    def parse_region(self, response):
        # URLS for each region are in table. Extract them here and follow each of them. Leads to next function.
        area_links = response.css("tbody a::attr(href)").getall()
        for link in area_links:
            if link.endswith(".shtml"):
                print("Going through hikes in: ",link.replace(".shtml", ""))
                yield response.follow(link, callback=self.parse_area)

    def parse_area(self, response):
        # extract all hike links from each area page
        for row in response.css("table.table1 tbody tr"):
            relative_url = row.css("td a::attr(href)").get()
            full_url = response.urljoin(relative_url)
            name = row.css("td a::text").get().strip()

            yield response.follow(
                full_url,
                callback=self.parse_hike,
                meta={"name": name, "url": full_url}
            )

    def parse_hike(self, response):
       grade_count = len(response.css("div.grade img"))
       bog_count = len(response.css("div.bog img"))
       terrain  = response.xpath("//h2[contains(text(), 'Terrain')]/following-sibling::p[1]/text()").get().strip()
       if grade_count>0 and bog_count>0:
            yield{
                "name": response.meta["name"],
                "url": response.meta["url"],
                "grade": grade_count,
                "bog": bog_count,
                "terrain": terrain
            }
