import requests
from bs4 import BeautifulSoup
import json

# URL de la page à scrapper
url = "https://etudescreatives.com/decryptage/lexique-jeu-video-vocabulaire-gamer/"

# Requête HTTP pour obtenir le contenu de la page
response = requests.get(url)
response.raise_for_status()  # Vérifie si la requête a réussi

# Parse le contenu HTML de la page
soup = BeautifulSoup(response.content, "html.parser")

# Trouver les sections contenant les mots et les définitions
lexique_dict = {}
current_term = None
# selection section def
section = soup.find_all("div", class_="elementor-widget-container" )[17]

items = section.find_all("p")
# on  enlève les 3 premieres
def_items = items[3:]


lexique_dict = {}
for item in def_items :
   try :
        word = item.find("strong").text
        if word is None :
            raise AttributeError(" ")
        definition = item.text
        print (definition)
        if ':' in definition :
            definition = definition.split(':',1)
            word = definition[0].strip()
            defi = definition[1].strip()
            print(word)
            print(defi)
            lexique_dict[word]= defi

   except AttributeError as e :
       print(f"Erreur: {e}")
       print(f"Problème avec l'élément: {item}")


# Sauvegarder les résultats dans un fichier JSON
with open("lexique_jeux_video.json", "w", encoding="utf-8") as f:
    json.dump(lexique_dict, f, ensure_ascii=False, indent=4)

print("Données scrappées et sauvegardées dans lexique_jeux_video.json")
print (f"Nombre d'éléments dans le dictionnaire : {len(lexique_dict)} ")
