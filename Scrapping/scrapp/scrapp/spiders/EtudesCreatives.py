import scrapy
import re



class CampusGamingSpider(scrapy.Spider):
    name = "etudes_creatives"
    allowed_domains = ["etudescreatives.com"]
    start_urls = ["https://etudescreatives.com/decryptage/lexique-jeu-video-vocabulaire-gamer/"]
    total_terms_scrapped = 0
    def parse(self, response):
        """
         Parses the lexicon from etudescreatives.com to extract terms and their definitions.

    Args:
        response (scrapy.http.Response): The web page response object.

    Returns:
        dict: A dictionary containing terms and their definitions, which can be extracted with the -o output.json option.
    """
        section = response.xpath("/html/body/main/section[4]/div/div[2]/div/div[2]/div")

        # pour repèrer les definitions on selection les titres
        definitions = []
        words = []
        paragraphs= section.xpath(".//h2/following-sibling::p") # select tags <p> after <h2>

        for paragraph in paragraphs :
            word = paragraph.xpath(".//strong/em/text()").get()
            print(word)
            if word != None:
                words.append(word)
                definition = paragraph.xpath("text()").get()
                # del word in the definition
                definition = definition.replace(word,"").strip()
                print(definition)
                definitions.append(definition)

        definition= remove_duplicates_list(definition)
        print (definitions)
        print (len(definition))
        print(words)
        print(len(words))
        """
        for word, definition in zip( words, definitions):
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
