import json
from collections import defaultdict

phrases_file: str = "russian_english_phrases.txt"
json_file: str = "russian_english_phrases.json"
duplicates_file: str = "duplicates.json"

phrase_mapping: dict = defaultdict(str)
duplicates: dict = {}

# Transition from delimited text to JSON
with (open(phrases_file, "r", encoding="utf-8") as pf,
      open(json_file, "w", encoding="utf-8") as jf,
      open(duplicates_file, "w", encoding="utf-8") as df):
    phrases = pf.readlines()

    for phrase in phrases:
        if "|" in phrase:
            phrases_list = list(map(str.strip, phrase.split("|")))
            phrase_rus = phrases_list[0]
            phrases_eng = phrases_list[1:]  # Everything from the list except the first element

            if phrase_mapping[phrase_rus] != "":  # Search for duplicates
                duplicates[phrase_rus] = phrases_eng

            phrase_mapping[phrase_rus] = phrases_eng

    if len(phrase_mapping) > 0:
        json.dump(phrase_mapping, jf, ensure_ascii=False, indent=2)
    if len(duplicates) > 0:
        json.dump(duplicates, df, ensure_ascii=False, indent=2)
