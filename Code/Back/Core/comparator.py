import jellyfish


class Comparator:
    @staticmethod
    def find_nearest_reference_index(user_input_without_punctuation_lower, references_lower: list[str]) -> tuple[int, float]:
        max_ratio: float = 0
        max_index: int = 0

        for i, reference in enumerate(references_lower):
            user_string = ''.join(user_input_without_punctuation_lower)
            reference_string = references_lower[i]

            current_ratio = jellyfish.jaro_distance(user_string, reference_string)

            if current_ratio > max_ratio:
                max_ratio = current_ratio
                max_index = i

        return max_index, max_ratio
