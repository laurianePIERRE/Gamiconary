import scrapy
import re


class CampusGamingSpider(scrapy.Spider):
    name = "campus_gaming"
    allowed_domains = ["gamingcampus.fr"]
    start_urls = ["https://gamingcampus.fr/boite-a-outils/lexique-du-jeu-video-100-mots-du-jeu-video.html"]

    def parse(self, response):
        items = response.xpath("//*[@id='a']/div/div/div")
        words = items.xpath("//strong/text()").getall()

        # cleanning words : remove spaces, \n and :
        cleaned_words = []
        for word in words:
            word= re.sub(" : *","",word)
            word = re.sub(r"\n *",'',word)
            cleaned_words.append(word)
        print(cleaned_words)

        definitions = items.xpath("./div/p/").xpath("string()").getall()
        # cleaning definition : remove «\xa0
        cleaned_definitions = []
        for definition in definitions:
            definition = re.sub("«\xa0","",definition)
            definition = re.sub(r"\xa0»","",definition)
            cleaned_definitions.append(definition)
        print( "----------------------- definition")
        print(cleaned_definitions)