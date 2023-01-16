import os
from pathlib import Path


class FileOperations:
    @staticmethod
    def find_or_create_file(filename: str, levelup: int = 2) -> str:
        if os.path.exists(filename):  # If file exist in app directory
            return filename
        else:  # If file doesn't exist in app directory, start search in all project directories
            for root, dirs, files in os.walk(Path(__file__).parents[levelup]):
                if filename in files:
                    return os.path.join(root, filename)

        # File doesn't exist in all project directories
        with open(filename, 'w'):  # Create file
            pass
        return filename

    @staticmethod
    def read_phrases(file_path: str) -> dict:
        phrase_mapping: dict = {}

        with open(file_path, 'r', encoding='utf-8') as phrf:
            for string in phrf.readlines():
                if string[0] != '#' and '||' in string:  # No comment line and contains rus-eng separator
                    phrases_pair = list(map(str.strip, string.split("||")))

                    if len(phrases_pair) > 2:
                        print(f'Error. String contains {len(phrases_pair)} "||" separators: ' + string +
                              '. String must contain only one "||" separator between phrases in different languages')
                    else:
                        rus_part, eng_part = phrases_pair[0], phrases_pair[1]

                        if "|" in eng_part:  # Multiple english phrases
                            eng_part = list(map(str.strip, eng_part.split('|')))  # Just split into separate english phrases

                        if "|" in rus_part:  # Multiple russian phrases
                            rus_part = list(map(str.strip, rus_part.split('|')))  # Split into separate russian phrases...
                            for rus_phrase in rus_part:
                                phrase_mapping[rus_phrase] = eng_part  # ... and save separate items

                        else:  # Single russian phrase
                            phrase_mapping[rus_part] = eng_part

        return phrase_mapping

    @staticmethod
    def read_repetitions(file_path: str) -> dict:
        ...

    @staticmethod
    def save_repetitions(file_path: str, repetitions: dict) -> dict:
        ...
