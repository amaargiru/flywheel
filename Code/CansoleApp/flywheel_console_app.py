import json
import os
from collections import defaultdict
from pathlib import Path

phrases_file: str = "russian_english_phrases.txt"
json_file: str = "russian_english_phrases.json"
duplicates_file: str = "duplicates.json"

phrase_mapping: dict = defaultdict(str)
duplicates_and_errors: list = []
phrases_without_diplicates: list = []


def find_file_in_project_directory(file_name):
    if os.path.exists(file_name):
        return file_name
    # If files doesn't exist in app directory, start search in all project directories
    else:
        for root, dirs, files in os.walk(Path(__file__).parents[2]):
            if file_name in files:
                return os.path.join(root, file_name)


with (open(find_file_in_project_directory(phrases_file), "r+", encoding="utf-8") as phrf,
      open(find_file_in_project_directory(json_file), "w", encoding="utf-8") as jsonf,
      open(find_file_in_project_directory(duplicates_file), "w", encoding="utf-8") as dupf):
    phrases_file_content = phrf.readlines()  # Phrases + comments

    # Transition from delimited text to JSON
    for string in phrases_file_content:
        if string[0] == "#" or string == "\n":
            phrases_without_diplicates.append(string)  # Just save comment string or empty string
        elif "||" in string:
            phrases_list = list(map(str.strip, string.split("||")))
            if len(phrases_list) > 2:
                duplicates_and_errors.append(f"Error. String contains {len(phrases_list)} '||' delimeters: " + string +
                                             ". String must contains only one '||' delimeter between phrases in different languages")
            else:
                rus_part, eng_part = phrases_list[0], phrases_list[1]

                if "|" in eng_part:  # Multiple english phrases
                    eng_part = list(map(str.strip, eng_part.split("|")))  # Just split into separate english phrases

                if "|" not in rus_part:  # Single russian phrase
                    if phrase_mapping[rus_part] != "":  # Search for duplicates
                        duplicates_and_errors.append(f"Duplicate: '{string}'")
                    else:
                        phrase_mapping[rus_part] = eng_part
                        # Save delimited text without duplicates (text cleanup)
                        # Text is compiled from different sources and definitely contains duplicates
                        phrases_without_diplicates.append(string)

                else:  # Multiple russian phrases
                    rus_part = list(map(str.strip, rus_part.split("|")))  # Split into separate russian phrases...
                    for rus_phrase in rus_part:
                        if phrase_mapping[rus_phrase] == eng_part:  # Search for duplicates
                            duplicates_and_errors.append(f"Duplicate: '{rus_phrase}' in '{string}'")
                        else:
                            phrase_mapping[rus_phrase] = eng_part  # ... and save separate items
                            # Save delimited text without duplicates (text cleanup)
                            # Text is compiled from different sources and definitely contains duplicates
                            if string not in phrases_without_diplicates:
                                phrases_without_diplicates.append(string)

        else:
            duplicates_and_errors.append(f"Error. '{string}' doesn't contains '||' delimeter")

    # Erase the file content before saving
    phrf.truncate(0)
    phrf.seek(0)

    # Save phrases without duplicates
    for string in phrases_without_diplicates:
        phrf.write(string)

    # Save JSON
    if len(phrase_mapping) > 0:
        json.dump(phrase_mapping, jsonf, ensure_ascii=False, indent=2)

    # Save list of duplicates (for info purposes only)
    if len(duplicates_and_errors) > 0:
        json.dump(duplicates_and_errors, dupf, ensure_ascii=False, indent=2)
