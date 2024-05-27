import scrapy
from scrapy import Selector
import re

class IgnLexiconSpider(scrapy.Spider):
    name = "ign_lexicon"
    allowed_domains = ["www.ign.com"]
    start_urls = ["https://www.ign.com/wikis/gaming-terms-lexicon/A/",
                  "https://www.ign.com/wikis/gaming-terms-lexicon/B/",
                  "https://www.ign.com/wikis/gaming-terms-lexicon/C/",]
    """
                  "https://www.ign.com/wikis/gaming-terms-lexicon/D/",
                  "https://www.ign.com/wikis/gaming-terms-lexicon/E/",
                  "https://www.ign.com/wikis/gaming-terms-lexicon/F/",
                  "https://www.ign.com/wikis/gaming-terms-lexicon/G/",
                  "https://www.ign.com/wikis/gaming-terms-lexicon/H/",
                  "https://www.ign.com/wikis/gaming-terms-lexicon/I/",
                  "https://www.ign.com/wikis/gaming-terms-lexicon/J/",
                  "https://www.ign.com/wikis/gaming-terms-lexicon/K/",
                  "https://www.ign.com/wikis/gaming-terms-lexicon/L/",
                  "https://www.ign.com/wikis/gaming-terms-lexicon/M/",
                  "https://www.ign.com/wikis/gaming-terms-lexicon/N/",
                  "https://www.ign.com/wikis/gaming-terms-lexicon/O/",
                  "https://www.ign.com/wikis/gaming-terms-lexicon/P/",
                  "https://www.ign.com/wikis/gaming-terms-lexicon/Q/",
                  "https://www.ign.com/wikis/gaming-terms-lexicon/R/",
                  "https://www.ign.com/wikis/gaming-terms-lexicon/S/",
                  "https://www.ign.com/wikis/gaming-terms-lexicon/T/",
                  "https://www.ign.com/wikis/gaming-terms-lexicon/U/",
                  "https://www.ign.com/wikis/gaming-terms-lexicon/V/",
                  "https://www.ign.com/wikis/gaming-terms-lexicon/W/",
                  "https://www.ign.com/wikis/gaming-terms-lexicon/X/",
                  "https://www.ign.com/wikis/gaming-terms-lexicon/Y/",
                  "https://www.ign.com/wikis/gaming-terms-lexicon/Z/",]
"""
    # variable globale pour suivre le nombre de termes scrappés

    total_terms_scrapped = 0


    def __init__(self,*args,**kwargs):
        super(IgnLexiconSpider, self).__init__(*args,**kwargs)
        # Reinizalize viable each excute spider
        self.total_terms_scrapped =0
    def parse(self, response):
        sections = response.xpath("//section[@class='content']")
        print("total : ",self.total_terms_scrapped)
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


        print (" le documents se compose de ",len(words)," mots, et donc ",len(final_definitions), " definitions")
        for word,definition in  zip(words,final_definitions):
            # increments
            self.total_terms_scrapped +=1
            yield {
                "EN" : word,
                "definition":definition
            }
        print("______________________________________________________________________________________________________")
        print("total : ", self.total_terms_scrapped)
    def Close (self, reason):
        print("Nombre total de termes scrappés :",self.total_terms_scrapped)
