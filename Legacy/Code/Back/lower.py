from typing import List


class Lower:
    @staticmethod
    def list_lower(input_list: list) -> list:
        lower_list: list = [ch.lower() for ch in input_list]
        return lower_list

    @staticmethod
    def references_lower(references: List[str]) -> List[str]:
        references_lower: List[str] = [ref.lower() for ref in references]
        return references_lower
