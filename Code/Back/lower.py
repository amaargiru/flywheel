class Lower:
    @staticmethod
    def list_lower(input_list: list) -> list:
        lower_list: list = []

        for ch in input_list:
            lower_list.append(ch.lower())

        return lower_list

    @staticmethod
    def references_lower(references: list[str]) -> list[str]:
        references_lower: list[str] = []

        for ref in references:
            references_lower.append(ref.lower())

        return references_lower
