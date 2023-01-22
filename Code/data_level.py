import sys
from datetime import datetime

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
                        "translate": eng_part,
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
