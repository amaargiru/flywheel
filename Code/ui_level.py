from data_level import DataOperations as dop


class UiOperations:
    @staticmethod
    def user_session(phrase: str, repetition: dict) -> float:
        """Console user interface"""
        user_input: str = input(f"Enter phrase \"{phrase}\" in english: ")
        dist = dop.find_max_jaro_distance(user_input, repetition["translations"])

        pass
        pass
