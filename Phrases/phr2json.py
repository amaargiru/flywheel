import json

phrases_file: str = "russian_english_phrases.txt"
json_file: str = "russian_english_phrases.json"

mapping: dict = {}

# Transition from delimited text to JSON
with (open(phrases_file, "r", encoding="utf-8") as pf, open(json_file, "w", encoding="utf-8") as jf):
    phrases = pf.readlines()

    for phrase in phrases:
        if "|" in phrase:
            rus, eng = map(str.strip, phrase.split("|"))
            mapping[eng] = rus

    json.dump(mapping, jf, ensure_ascii=False, indent=2)
