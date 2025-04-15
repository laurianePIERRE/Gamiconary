
import scrapy
import tldextract
import re
import os
from pathlib import Path
"""
# Configurer tldextract pour utiliser un répertoire de cache accessible

# Désactiver le cache de tldextract
extract = tldextract.TLDExtract(cache_dir=False)


cache_dir = Path(os.getenv('LOCALAPPDATA', '')) / 'tldextract_cache'

# Créer le répertoire de cache s'il n'existe pas
cache_dir.mkdir(parents=True, exist_ok=True)

# Afficher le répertoire de cache pour vérification
print(f"Using cache directory: {cache_dir}")

# Configurer tldextract pour utiliser ce répertoire de cache
extract = tldextract.TLDExtract(cache_dir=str(cache_dir))

"""
class CampusGamingSpider(scrapy.Spider):
    name = "playstation"
    allowed_domains = ["playstation.com"]
    start_urls = ["https://www.playstation.com/en-us/editorial/playstation-ultimate-gaming-glossary/"]
    total_terms_scrapped = 0
    def parse(self, response):
        """
         Parses the lexicon from gamingccampus.fr to extract terms and their definitions.

    Args:
        response (scrapy.http.Response): The web page response object.

    Returns:
        dict: A dictionary containing terms and their definitions, which can be extracted with the -o output.json option.
    """

        print("hellllllllllllllllllllloooooo")
        sections = response.xpath("/html/body/div[2]/div/div[1]/div/div[2]/section/div/div")
        other_sections = response.xpath("/html/body/div[2]/div/div[1]/div/div[2]/section/div/div")
        print('length sections : ',len(other_sections))
        cleaned_words = []
        all_definition =[]
        all_words=[]
        cleaned_definition = []
    """
        for section in sections:
            elements = section.xpath("./div/div/div[3]/div/div/ul/li" )
            for element in elements :
                word = element.xpath(".//b/text()").getall()
                all_words.append(word)
                definition = element.xpath(".//text()").getall()
                all_definition.append(definition)
            print(all_definition)
            print("-------------------------------------------------------------------------")
            print(all_words)
            print("length definitions :", len(all_definition))
            print(" length word : ", len(all_words))
        """
    """
        for word, definition in zip( cleaned_words,all_definition):
            self.total_terms_scrapped += 1
            yield {
                "FR": word,
                "definition": definition
            }

        """
    def Close(self, reason):
        print("Nombre total de termes scrappés :", self.total_terms_scrapped)

# scrapy crawl campus_gaming -o output.json
        #print(all_definition)
        #print (len(all_definition))
        #print (len(cleaned_words))

        #print(cleaned_words)
        #print(len(cleaned_words))

def remove_duplicates_list(my_list) :
    """

    :param liste:
    :return:
    """
    unique_list = []
    seen = set()
    for item in my_list :
        if item is not seen :
            unique_list.append(item)
            seen.add(item)
    return unique_list
