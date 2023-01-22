import builtins
import re
import sys
from datetime import datetime
from re import Pattern
from typing import List

import jellyfish

datetime_format: str = "%Y.%m.%d %H:%M:%S"


class DataOperations:
    @staticmethod
    def data_assessment(phrases: dict, repetitions: dict) -> (bool, str):
        if not isinstance(phrases, dict):
            print(f"Cant parse phrases file")
            sys.exit()

        if not isinstance(repetitions, dict):
            print(f"Cant parse repetitions file")
            sys.exit()

        if len(phrases) == 0 and len(repetitions) == 0:
            return False, "Both structures have zero length"
        else:
            return True, "No data assessment errors"

    @staticmethod
    def merge(phrases: dict, repetitions: dict) -> (bool, str):
        """Merge new phrases into general dictionary"""
        no_added_message: str = "No new phrases added"
        new_phrases: int = 0

        if len(phrases) == 0:
            return False, no_added_message
        else:
            for rus_part, eng_part in phrases.items():
                if rus_part not in repetitions:
                    repetitions[rus_part] = {
                        "translations": eng_part,
                        "attempts": [],
                        "time_to_repeat": datetime.now().strftime(datetime_format)}  # Recommendation to check this phrase right now
                    new_phrases += 1

        return (False, no_added_message) if new_phrases == 0 else (True, f"Added {new_phrases} new phrases")

    @staticmethod
    def determine_next_phrase(repetitions: dict) -> str:
        """Determine phrase for next user session"""
        recommended_phrase: str = ""
        min_time_to_repeat = datetime.max

        for current_phrase, value in repetitions.items():
            current_time_to_repeat = datetime.strptime(value["time_to_repeat"], datetime_format)
            if current_time_to_repeat < min_time_to_repeat:
                recommended_phrase = current_phrase
                min_time_to_repeat = current_time_to_repeat

        return recommended_phrase

    @staticmethod
    def update_repetitions(repetitions: dict, current_phrase: str, user_result: float) -> str:
        ...

    @staticmethod
    def cleanup_user_input(user_input: str) -> str:
        MAX_STRING_SIZE: int = 200
        comma_pattern: Pattern[str] = re.compile(r"(,){2,}")
        white_list: str = " ?!.,:;'"  # Allow symbols (+ alpha-numeric)

        user_input = user_input[:MAX_STRING_SIZE]  # Length limit
        user_input = user_input.strip()  # Remove leading and trailing whitespace
        user_input = ''.join(ch for ch in user_input if ch.isalnum() or ch in white_list)  # Delete all unwanted symbols
        user_input = user_input.replace("\t", " ")  # Replace tabs with spaces
        user_input = ' '.join(user_input.split())  # Replace multiple spaces with one
        user_input = re.sub(comma_pattern, ",", user_input)  # Replace multiple commas with one

        return user_input

    @staticmethod
    def find_max_jaro_distance(user_input: str, translations: str | List[str]) -> (float, str):
        max_distance: float = 0
        best_translation: int = 0

        def compact(input_string: str) -> str:
            return ''.join(ch for ch in input_string if ch.isalnum() or ch == ' ')

        # Cleanup and 'compactify' user input ('I   don't know!!!😀' -> 'i dont know')
        user_input = compact(DataOperations.cleanup_user_input(user_input).lower())

        # 'Compactify' translations
        translations = compact(translations.lower()) if isinstance(translations, str) else [compact(t.lower()) for t in translations]

        if isinstance(translations, str):
            distance = jellyfish.jaro_distance(user_input, translations)
            return distance, translations
        else:
            for t in translations:
                current_distance = jellyfish.jaro_distance(user_input, t)

                if current_distance > max_distance:
                    max_distance = current_distance
                    best_translation = t

            return max_distance, best_translation
