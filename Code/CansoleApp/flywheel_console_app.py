import json
import os
from collections import defaultdict
from pathlib import Path

phrases_file: str = "russian_english_phrases.txt"
json_file: str = "russian_english_phrases.json"
duplicates_file: str = "duplicates.json"

phrase_mapping: dict = defaultdict(str)
duplicates_and_errors: list = []


def find_file_in_project_directories(file_name):
    if os.path.exists(file_name):
        return file_name
    # If files doesn't exist in app directory, start search in all project directories
    else:
        for root, dirs, files in os.walk(Path(__file__).parents[2]):
            if file_name in files:
                return os.path.join(root, file_name)


with (open(find_file_in_project_directories(phrases_file), "r+", encoding="utf-8") as phrf,
      open(find_file_in_project_directories(json_file), "w", encoding="utf-8") as jsonf,
      open(find_file_in_project_directories(duplicates_file), "w", encoding="utf-8") as dupf):
    phrases_file_content = phrf.readlines()  # Phrases + comments

    # Erase the file content before saving without duplicates
    phrf.truncate(0)
    phrf.seek(0)

    # Transition from delimited text to JSON
    for string in phrases_file_content:
        if string[0] == "#" or string == "\n":
            phrf.write(string)  # Just save comment string or empty string
        elif "||" in string:
            phrases_list = list(map(str.strip, string.split("||")))
            if len(phrases_list) > 2:
                duplicates_and_errors.append(f"Error. String contains {len(phrases_list)} '||' delimeters: " + string +
                                             ". String must contains only one '||' delimeter between phrases in different languages")
            else:
                phrase_rus, phrases_eng = phrases_list[0], phrases_list[1]

                if phrase_mapping[phrase_rus] != "":  # Search for duplicates
                    duplicates_and_errors.append(f"Duplicate: {string}")
                else:
                    phrase_mapping[phrase_rus] = phrases_eng
                    # Save delimited text without duplicates (text cleanup)
                    # Text is compiled from different sources and definitely contains duplicates
                    phrf.write(string)
        else:
            duplicates_and_errors.append("Error. String doesn't contains '||' delimeter")

    # Save JSON
    if len(phrase_mapping) > 0:
        json.dump(phrase_mapping, jsonf, ensure_ascii=False, indent=2)

    # Save list of duplicates (for info purposes only)
    if len(duplicates_and_errors) > 0:
        json.dump(duplicates_and_errors, dupf, ensure_ascii=False, indent=2)
