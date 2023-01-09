import json

phrases_file: str = "russian_english_phrases.txt"
json_file: str = "russian_english_phrases.json"

phrase_mapping: dict = {}

# Transition from delimited text to JSON
with (open(phrases_file, "r", encoding="utf-8") as pf, open(json_file, "w", encoding="utf-8") as jf):
    phrases = pf.readlines()

    for phrase in phrases:
        if "|" in phrase:
            phrases_list = list(map(str.strip, phrase.split("|")))
            phrase_rus = phrases_list[0]
            phrases_eng = phrases_list[1:]  # Everything from the list except the first element
            phrase_mapping[phrase_rus] = phrases_eng

    json.dump(phrase_mapping, jf, ensure_ascii=False, indent=2)
