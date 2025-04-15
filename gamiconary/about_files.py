"""

combine french files and english files

match french and english
"""
import os
import json

file_path = "C:/Users/Lauriane/OneDrive/Documents/Master/Projet Alternance/Gamiconay_app/Data/"

def load_json(file_path) :
    with open (file_path, 'r', encoding='utf-8') as file :
        return json.load(file)


# Combine files into only file

def combine_languages(fr_dict, en_dict) :
    combined = []

    # si les listes de mots sont de la même longueur et dans le même ordre

    for i, fr_entry in enumerate(fr_dict):
        fr_word = fr_entry["FR"]
        fr_definition = fr_entry["definition"]

        if i < len(en_dict) :
            en_word = en_dict[i]['EN']
            en_definition = en_dict[i]["definition"]

            combined.append({
                "FR" :fr_word,
                "EN" : en_word,
                "definition" : {
                    "FR": fr_definition,
                    "EN":en_definition
                }
            })
    return combined

def save_json(data, file_path) :
    with open(data, file_path, "w", encoding='utf-8') as file :
        json.dump(data, file, ensure_ascii=False, indent=4)


def combine_words_optimized(fr_dict, en_dict):
    combined = []

    # Parcourir les mots français
    for fr_word, fr_definition in fr_dict.items():
        # Chercher l'équivalent en anglais (si présent)
        en_word = next((en_word for en_word in en_dict if en_dict.get(en_word, '') == fr_definition), None)
        en_definition = en_dict.get(en_word, None)

        # Créer une entrée combinée
        combined.append({
            "FR": fr_word,
            "EN": en_word if en_word else "Non disponible",
            "définition": {
                "FR": fr_definition,
                "EN": en_definition if en_definition else "Non disponible"
            }
        })

    return combined


fr_file = file_path+"campus_gaming_clean.json"
en_file = file_path+"ign_modify.json"

fr_data=load_json(fr_file)
en_data = load_json(en_file)

combined_data =combine_languages(fr_data,en_data)
print(combined_data)
output_file=file_path+"combine_test.json"
save_json(combined_data,output_file)