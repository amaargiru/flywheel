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
    def merge(phrases: dict, repetitions: dict) -> str:
        no_added_message: str = "No new phrases added"
        new_phrases: int = 0

        if len(phrases) == 0:
            return no_added_message
        else:
            for rus_part, eng_part in phrases.items():
                if rus_part not in repetitions:
                    repetitions[rus_part] = {
                        "translate": eng_part,
                        "attempts": [],
                        "time_to_repeat": datetime.now().strftime(datetime_format)}  # Recommendation to check this phrase right now
                    new_phrases += 1

        return no_added_message if new_phrases == 0 else f"Added {new_phrases} new phrases"

    @staticmethod
    def determine_current_phrase(repetitions: dict) -> str:
        current_phrase: str = ""
        current_time_to_repeat = datetime.max

        for k, v in repetitions.items():
            time_to_repeat = datetime.strptime(v["time_to_repeat"], datetime_format)
            if time_to_repeat < current_time_to_repeat:
                current_phrase = k
                current_time_to_repeat = time_to_repeat

        return current_phrase

    @staticmethod
    def update_repetitions(repetitions: dict, current_phrase: str, user_result) -> str:
        ...
