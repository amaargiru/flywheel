from difflib import SequenceMatcher
from complicator import ComplexUserInput

class Finder:
    @staticmethod
    def find_nearest_reference_index(user_input_without_punctuation_lower: ComplexUserInput, references_lower: list[str]):
        for i, reference in enumerate(references_lower):
            s = SequenceMatcher(None, "abcd", "bcde")
