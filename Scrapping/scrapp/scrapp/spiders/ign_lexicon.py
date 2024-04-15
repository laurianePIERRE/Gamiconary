import scrapy
from scrapy import Selector
import re

class IgnLexiconSpider(scrapy.Spider):
    name = "ign_lexicon"
    allowed_domains = ["www.ign.com"]
    start_urls = ["https://www.ign.com/wikis/gaming-terms-lexicon/A/"]

    def parse(self, response):
        sections = response.xpath("//section[@class='content']")

        # sans se soucier des balises <b>

        words = sections.xpath("//span[@class='mw-headline']/text()").getall()
        print("words", words)
        definitions = sections.xpath("//section[@class='jsx-2191675443 jsx-2580457997 jsx-28683165 wiki-section wiki-html']/p").getall()
        print("definition",definitions)

        # pour les 4 premieres récupèrer la lettre dans les balise <b> et concéténer dan un élément tant qu'il y a présence d'une balise b

        concatenated_texts = []
        for definition in definitions[0]:
            sel = Selector(text=definition)
            full_text = sel.xpath("string()").get()
            concatenated_texts.append(full_text)

        # remplacer

        definitions[0] = "".join(concatenated_texts)
        final_definitions = []
        for definition in definitions:
            sel= Selector(text=definition)
            clean_text = sel.xpath("string()").get()
            clean_text = re.sub("\n",'',clean_text)
            final_definitions.append(clean_text)


     #   print("--------------------------------------------------------------------------------")
      #  print(final_definitions[0:4])
       # print(len(final_definitions))
        #print(len(words))

        print (final_definitions)
        for word,definition in  zip(words,final_definitions):
            yield {
                "EN" : word,
                "definition":definition
            }

