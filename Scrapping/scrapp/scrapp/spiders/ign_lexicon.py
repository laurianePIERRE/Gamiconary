import scrapy


class IgnLexiconSpider(scrapy.Spider):
    name = "ign_lexicon"
    allowed_domains = ["www.ign.com"]
    start_urls = ["https://www.ign.com/wikis/gaming-terms-lexicon/A/"]

    def parse(self, response):
        sections = response.xpath("//section[@class='content']")

        words = sections.xpath("//span[@class='mw-headline']/text()").getall()
        definitions_elements  = sections.xpath("//section[@class='jsx-2191675443 jsx-2580457997 jsx-28683165 wiki-section wiki-html']/p")


# Afin de contournee les balises <b> nous devons traiter chaque definition$

        current_definition = ""
        current_letter = None

        definitions = []

        for element in definitions_elements :
            # pour chaque paragraph obtenire le text et elimine les balises <b>
            paragraph_text = ''.join(element.xpath(".//text()").getall()).strip()
            letter = element.xpath(".//b/text()").get()

            # Si le texte dans le texte dans la balise <b> est different de la lettre actuelle, ajouter a la definitionv
            if letter != current_letter and current_definition:
                definitions.append((current_letter, current_definition.strip()))
                current_definition=''

            current_letter = letter

            if paragraph_text:
                current_definition += " "+paragraph_text

        if current_definition:
            definitions.append((current_letter, current_definition.strip()))


        print(definitions)
        print(len(words))
        print(len(definitions))
        if len(words) == len(definitions):
           for word, definition in zip(words,definitions):
               print(word,definition)
               yield {
                   "EN" : word,
                   "definition":definition
               }
        else:
            print ("erreur ")


