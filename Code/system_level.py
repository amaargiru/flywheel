class FileOperations:
    @staticmethod
    def find_or_create_file(filename: str) -> str:
        ...

    @staticmethod
    def read_phrases(file_path: str) -> dict:
        ...

    @staticmethod
    def read_repetitions(file_path: str) -> dict:
        ...

    @staticmethod
    def save_repetitions(file_path: str, repetitions: dict) -> dict:
        ...
