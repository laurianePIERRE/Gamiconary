
import scrapy
import re



class CampusGamingSpider(scrapy.Spider):
    name = "campus_gaming"
    allowed_domains = ["gamingcampus.fr"]
    start_urls = ["https://gamingcampus.fr/boite-a-outils/lexique-du-jeu-video-100-mots-du-jeu-video.html"]
    total_terms_scrapped = 0
    def parse(self, response):
        """
         Parses the lexicon from gamingccampus.fr to extract terms and their definitions.

    Args:
        response (scrapy.http.Response): The web page response object.

    Returns:
        dict: A dictionary containing terms and their definitions, which can be extracted with the -o output.json option.
    """
        sections = response.xpath("/html/body/main/article/section")
        cleaned_words = []
        all_definition =[]
        all_words=[]
        cleaned_definition = []
        for section, i in zip (sections, range(len(sections))) :
            words_element = section.xpath("./div/div/div" )
            for element in words_element:
                words = element.xpath("./strong/text()").getall()
                for word in words:
                    word = re.sub(" : *", "", word)
                    word = re.sub(r"\n *", '', word)
                    cleaned_words.append(word)

                definitions = element.xpath("string(./div/p)").getall()
                for definition in definitions:
                    definition = re.sub("«\xa0", "", definition)
                    definition = re.sub(r"\xa0»", "", definition)
                    cleaned_definition.append(definition)
        all_words += cleaned_words

        all_definition += cleaned_definition
        all_definition = remove_duplicates_list(all_definition)
        all_definition = [x for x in all_definition if x != '']
        # create the dictionnary
        for word, definition in zip( cleaned_words,all_definition):
            self.total_terms_scrapped += 1
            yield {
                "FR": word,
                "definition": definition
            }


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
