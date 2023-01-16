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
        ...

    @staticmethod
    def read_repetitions(file_path: str) -> dict:
        ...

    @staticmethod
    def save_repetitions(file_path: str, repetitions: dict) -> dict:
        ...
