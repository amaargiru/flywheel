class DataOperations:
    @staticmethod
    def data_assessment(phrases: dict, repetitions: dict) -> (bool, str):
        ...

    @staticmethod
    def merge(phrases: dict, repetitions: dict) -> str:
        ...

    @staticmethod
    def update_repetitions(repetitions: dict, current_phrase: str, user_result) -> str:
        ...

    @staticmethod
    def determine_current_phrase(repetitions: dict) -> str:
        ...
