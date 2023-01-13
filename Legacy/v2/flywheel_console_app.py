import json
from collections import defaultdict
from types import SimpleNamespace

phrases_file: str = "phrases.txt"
progress_file: str = "progress.json"

duplicates_and_errors: list = []
phrases_without_diplicates: list = []

with (open(phrases_file, "r+", encoding="utf-8") as phrf,
      open(progress_file, "r+", encoding="utf-8") as jsonf):
    phrase_mapping = json.load(jsonf)
    #received = json.loads(phrf.readlines(), object_hook=lambda h: SimpleNamespace(**h))
    # Transition from delimited text to JSON
    for string in phrf.readlines():
        if string[0] == "#" or string == "\n":
            phrases_without_diplicates.append(string)  # Just save comment string or empty string
        elif "||" in string:
            phrases_list = list(map(str.strip, string.split("||")))
            if len(phrases_list) > 2:
                print(f"Error. String contains {len(phrases_list)} '||' separators: " + string +
                      ". String must contains only one '||' separator between phrases in different languages")
            else:
                rus_part, eng_part = phrases_list[0], phrases_list[1]

                if "|" in eng_part:  # Multiple english phrases
                    eng_part = list(map(str.strip, eng_part.split("|")))  # Just split into separate english phrases

                if "|" not in rus_part:  # Single russian phrase
                    if len(phrase_mapping[rus_part]) != 0:  # Search for duplicates
                        print(f"Duplicate: '{string}'")
                    else:
                        phrase_mapping[rus_part] = {"translate": eng_part, "attempts": []}
                        # Save delimited text without duplicates (text cleanup)
                        # Text is compiled from different sources and definitely contains duplicates
                        phrases_without_diplicates.append(string)

                else:  # Multiple russian phrases
                    rus_part = list(map(str.strip, rus_part.split("|")))  # Split into separate russian phrases...
                    for rus_phrase in rus_part:
                        if len(phrase_mapping[rus_phrase]) != 0:  # Search for duplicates
                            print(f"Duplicate: '{rus_phrase}' in '{string}'")
                        else:
                            phrase_mapping[rus_phrase] = {"translate": eng_part, "attempts": []}  # ... and save separate items
                            # Save delimited text without duplicates (text cleanup)
                            # Text is compiled from different sources and definitely contains duplicates
                            if string not in phrases_without_diplicates:
                                phrases_without_diplicates.append(string)
        else:
            print(f"Error. '{string}' doesn't contains '||' separator")

    # Erase the file content before modifying
    phrf.truncate(0)
    phrf.seek(0)
    # Save phrases without duplicates
    for string in phrases_without_diplicates:
        phrf.write(string)

    # Save JSON
    if len(phrase_mapping) > 0:
        json.dump(phrase_mapping, jsonf, ensure_ascii=False, indent=2)
