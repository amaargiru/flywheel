import re
import sys
from datetime import datetime, timedelta
from re import Pattern
from typing import List

import jellyfish

datetime_format: str = "%Y.%m.%d %H:%M:%S"
max_attempts_len: int = 10  # Limit for 'Attempts' list


class DataOperations:
    level_excellent: float = 0.99
    level_good: float = 0.97
    level_mediocre: float = 0.65

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
                        "time_to_repeat": datetime.now().strftime(datetime_format),  # Recommendation to check this phrase right now
                        "easiness_factor": 2.5,  # EF, how easy the card is (and determines how quickly the inter-repetition interval grows)
                        "repetition_number": 0,  # Number of times the card has been successfully recalled in a row
                        "attempts": []}  # Reserve field in case of transition from supermemo-2 to supermemo-18
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
    def update_repetitions(repetitions: dict, current_phrase: str, user_result: float):
        # Update list of attempts
        if len(repetitions[current_phrase]['attempts']) == max_attempts_len:
            repetitions[current_phrase]['attempts'].pop(0)
        repetitions[current_phrase]['attempts'].append((datetime.now().strftime(datetime_format), user_result))

        # Update whole repetition data
        repetitions[current_phrase] = DataOperations.supermemo2(repetitions[current_phrase], user_result)

    @staticmethod
    # https://en.wikipedia.org/wiki/SuperMemo
    def supermemo2(repetition: dict, user_result: float) -> dict:
        if user_result >= DataOperations.level_good:  # Correct response
            if repetition["repetition_number"] == 0:  # + 1 day
                repetition["time_to_repeat"] = (datetime.now() + timedelta(days=1)).strftime(datetime_format)
            elif repetition["repetition_number"] == 1:  # + 6 days
                repetition["time_to_repeat"] = (datetime.now() + timedelta(days=6)).strftime(datetime_format)
            else:  # + (6 * EF) days
                repetition["time_to_repeat"] = (datetime.now()
                                                + timedelta(days=6 * repetition["easiness_factor"])).strftime(datetime_format)
            repetition["repetition_number"] += 1
        else:  # Incorrect response
            repetition["time_to_repeat"] = (datetime.now()).strftime(datetime_format)  # Recommendation to repeat this phrase right now
            repetition["repetition_number"] = 0

        repetition["easiness_factor"] = repetition["easiness_factor"] + \
                                        (0.1 - (5 - 5 * user_result) * (0.08 + (5 - 5 * user_result) * 0.02))
        repetition["easiness_factor"] = max(repetition["easiness_factor"], 1.3)

        return repetition

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

        if isinstance(translations, str):
            translations = [translations]
        best_translation: str = translations[0]

        def compact(input_string: str) -> str:
            return ''.join(ch for ch in input_string if ch.isalnum() or ch == ' ')

        # Cleanup and 'compactify' user input ('I   don't know!!!😀' -> 'i dont know')
        user_input = compact(DataOperations.cleanup_user_input(user_input).lower())

        # 'Compactify' translations
        translations = [(t, compact(t.lower())) for t in translations]

        for translation, compact_translation in translations:
            current_distance = jellyfish.jaro_distance(user_input, compact_translation)

            if current_distance > max_distance:
                max_distance = current_distance
                best_translation = translation

            return max_distance, best_translation
