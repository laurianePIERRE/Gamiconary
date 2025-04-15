import json
import os
from pprint import pprint
from pymongo import MongoClient
import pandas as pd

from difflib import get_close_matches
# Configuration de la connexion mongoDB

JSON_DIR = "C:/Users/Lauriane/OneDrive/Documents/Master/Projet Alternance/Gamiconay_app/Data"

VALITED_TERMS = ("C:/Users/Lauriane/OneDrive/Documents/Master/Projet Alternance/Gamiconay_app/Data/Data_combined\
/french_lexicon_web_combined_clean.json")

def insert_json_files (directory, collection):
    """
    put termes in mongo database
    :param directory:  dir of json file
    :param collection: collection of terme in MongoDB database
    :return:
    """

    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            print(f"Traitement du fichier : {file_path}")
            with open(file_path, 'r', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                    if isinstance(data, dict):
                        # Vérification du format avant l'insertion
                        if 'FR' in data or 'EN_match' in data:
                            collection.insert_one(data)
                            print(f"Terme inséré : {data}")
                        else:
                            print(f"Format de données inattendu dans le fichier {filename} : {data}")
                    elif isinstance(data, list):
                        for terme in data:
                            if isinstance(terme, dict) and ('FR' in terme or 'EN' in terme):
                                collection.insert_one(terme)
                                print(f"Terme inséré : {terme}")
                                print("Ajout OK")
                            else:
                                print(f"Format de données inattendu dans le fichier {filename} : {terme}")
                    else:
                        print(f"Format de données inattendu dans le fichier {filename}")
                    print(f"Les données provenant du fichier {filename} ont été insérées avec succès.")
                except Exception as e:
                    print(f"Erreur pour l'insertion du fichier {filename}: {e}")



def insert_valided_file(filename):
  """
  insert a valided file in the Mongo database
  :param filename: file contents french and english terms 
  :return: database complited
  """
  collection = create_connection()
  with open(filename, 'r', encoding='utf-8') as file:
      try:
          data = json.load(file)
          if isinstance(data, dict):
              # Vérification du format avant l'insertion
              data["validated"] = True
              if 'FR' in data or 'EN_match' in data:
                  collection.insert_one(data)
                  print(f"Terme inséré : {data}")
              else:
                  print(f"Format de données inattendu dans le fichier {filename} : {data}")
          elif isinstance(data, list):
              valid_terms=[]
              for terme in data:
                  if isinstance(terme, dict) and ('FR' in terme or 'EN' in terme):
                      terme["validated"]= True
                      valid_terms.append(terme)
                  else :
                      print(f"Format de données inattendu dans le fichier {filename} : {terme}")
          if valid_terms:
              collection.insert_many(valid_terms)
              print(f"{len(valid_terms)}  termes ont été insérées avec succès.")
      except Exception as e :
          print(f"Erreur pour l'insertion du fichier {filename}: {e}")


def vizualize_data():
    collection = create_connection()
    data = list(collection.find())
    if not data:
        print("No data found")

    df = pd.DataFrame(data)

    if '_id' in df.columns:
        df.drop('_id',axis=1)
    print(df)

def load_json(file_path):
    """ Load a json file from the given path
    :param file_path: str
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError as e:
            print(f"Erreur lors du chargement du fichier {file_path}: {e}")
            return None

def combine_json_files(input_directory, output_file):
    """
    Combine all json files from the input_directory into one json file in the output_directory
    :param input_directory: str
    :param output_directory: str
    """
    combinedd_data=[]
    for filename in os.listdir(input_directory, ):
        if filename.endswith('.json'):
            file_path = os.path.join(input_directory, filename)
            print(f"Traitement du fichier : {file_path}")
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = load_json(file_path)
                if isinstance(data, list):
                    combinedd_data.extend(data)
                else :
                    print (f"Le fichier {f} n'est pas au format demandé")
            except Exception as e:
                print(f"Erreur pour le fichier {filename}: {e}")
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(combinedd_data, outfile, indent=4)
    print (f"Fichier combiné crée : {output_file}")

def empty_database():
    """
    Vide la base de données
    :param collection: collection de terme dans MongoDB database
    :return:
    """
    collection = create_connection()
    collection.delete_many({})
    print("Base de données vidée avec succès")

def create_connection():
    """
    Créer une connexion à MongoDB
    :return: Collection
    """
    try :
        client = MongoClient('mongodb://localhost:27017/')
        client.server_info()
        print("Connexion à MongoDB établie avec succès")
        db = client["Gamiconary"]
        collection=db['termes']
        return collection
    except Exception as e :
        print (f'Erreur lors de la connexion à MongoDB : {e}')
        return None

def display_collection():
    """
    Affiche tous les documents dans la base de données
    """
    collection = create_connection()
    cursor =  collection.find({'validated':True})
    found = False
    for doc in cursor:
        pprint(doc)
        print('-'*50)
        found = True

    if not found :
        print("Aucun terme valide trouvé dans la base de données.")


def empty_collection():
    collections = create_connection()
    collections.remove()
    print("Base de données vidée avec succès")

def count_terms_valid():
    """
    Compter le nombre de termes valides dans la base de données
    """
    collection = create_connection()
    if collection:
        count = collection.count_documents({})
        print(f"Nombre de termes valides dans la base de données : {count}")


def count_terms_to_valid() :
    collection=create_connection()
    if collection:
        # Requête
        resultats = collection.find({"validated": False})

        # Affichage
        count = collection.count_documents({"validated": False})
        print(f"{count} suggestion(s) non validée(s) trouvée(s) dans MongoDB :")
        for doc in resultats:
            print(f"- ID : {doc.get('_id')} | Terme : {doc.get('terme')} | Date : {doc.get('date')}")

FILE_COMBINED = "C:/Users/Lauriane/OneDrive/Documents/Master/Projet Alternance/Gamiconay_app/Data/Data_combined/english_french_combined.json"
print("lalala")
#empty_collection()
#insert_valided_file(FILE_COMBINED)
    # Afficher tous les documents
#display_collection()
    # compter le nombre de documents
print("_____________________________________________________________________________________________________")
#count_terms_valid()
count_terms_to_valid()