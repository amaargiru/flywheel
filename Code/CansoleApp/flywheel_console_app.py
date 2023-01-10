import json
from collections import defaultdict

phrases_file: str = "russian_english_phrases.txt"
json_file: str = "russian_english_phrases.json"
duplicates_file: str = "duplicates.json"

phrase_mapping: dict = defaultdict(str)
duplicates: dict = {}

with (open(phrases_file, "r+", encoding="utf-8") as pf,
      open(json_file, "w", encoding="utf-8") as jf,
      open(duplicates_file, "w", encoding="utf-8") as df):
    phrases = pf.readlines()

    # Erase the file content before saving w/o duplicates
    pf.truncate(0)
    pf.seek(0)

    # Transition from delimited text to JSON
    for phrase in phrases:
        if "|" in phrase:
            phrases_list = list(map(str.strip, phrase.split("|")))
            phrase_rus = phrases_list[0]
            phrases_eng = phrases_list[1:]  # Everything from the list except the first element

            if phrase_mapping[phrase_rus] != "":  # Search for duplicates
                duplicates[phrase_rus] = phrases_eng
            else:
                phrase_mapping[phrase_rus] = phrases_eng
                # Save delimited text w/o duplicates (text cleanup)
                # Text is compiled from different sources and definitely contains duplicates
                pf.write(phrase)

    # Save JSON
    if len(phrase_mapping) > 0:
        json.dump(phrase_mapping, jf, ensure_ascii=False, indent=2)

    # Save list of duplicates (for info purposes only)
    if len(duplicates) > 0:
        json.dump(duplicates, df, ensure_ascii=False, indent=2)
