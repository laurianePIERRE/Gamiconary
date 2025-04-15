import os
import json

def count_elements_in_json_files(directory):
    total_elements = 0
    count_files =0
    # Parcourir tous les fichiers et dossiers dans le répertoire donné
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                count_files += 1

                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        # Ajouter le nombre d'éléments dans ce dictionnaire au total
                        nb_terms = len(data)
                        total_elements += nb_terms
                        print(total_elements)
                except Exception as e:
                    print(f"Erreur lors de la lecture du fichier {file_path}: {e}")

    return total_elements,count_files


# Exemple d'utilisation :
directory_path_list = ('C:/Users/Lauriane/OneDrive/Documents/Master/Projet Alternance/Gamiconay_app/data_processing/Data/data_to_transform/Lexiques_Français/fichier.json/listes')
total_elements, count_file = count_elements_in_json_files(directory_path_list)
print("Nombre total d'éléments dans les fichiers JSON :", total_elements," dans ",count_file,' fichier')

directory_path_paragraph = ('C:/Users/Lauriane/OneDrive/Documents/Master/Projet Alternance/Gamiconay_app/data_processing/Data/data_to_transform/Lexiques_Français/fichier.json/paragraphes')
total_elements, count_file = count_elements_in_json_files(directory_path_paragraph)
print("Nombre total d'éléments dans les fichiers JSON :", total_elements," dans ",count_file,' fichier')

directory_path_tables = ('C:/Users/Lauriane/OneDrive/Documents/Master/Projet Alternance/Gamiconay_app/data_processing/Data/data_to_transform/Lexiques_Français/fichier.json/tables')
total_elements, count_file = count_elements_in_json_files(directory_path_tables)
print("Nombre total d'éléments dans les fichiers JSON :", total_elements," dans ",count_file,' fichier')