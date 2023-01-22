import colorama
from colorama import Fore

from data_level import DataOperations as dop


class UiOperations:
    @staticmethod
    def user_session(phrase: str, repetition: dict) -> float:
        """Console user interface"""
        user_input: str = input(f"Enter phrase \"{phrase}\" in english: ")
        distance, best_translation = dop.find_max_jaro_distance(user_input, repetition["translations"])

        colorama.init()

        if distance > dop.level_excellent:  # Phrases are identical
            print(Fore.GREEN + "Correct!")
        elif distance > dop.level_good:  # The phrases are very similar, perhaps a typo
            print(Fore.BLACK + "Almost correct. Right answer is: ", end="")
            print(Fore.BLACK + best_translation)
        elif distance > dop.level_mediocre:  # Phrases have a lot in common
            print(Fore.BLACK + "Not bad. ", end="")
            print(Fore.BLACK + "Right answer is: ", end="")
            print(Fore.BLACK + best_translation)
        else:
            print(Fore.RED + "Wrong. ", end="")  # There are too many mistakes
            print(Fore.BLACK + "Right answer is: ", end="")
            print(Fore.GREEN + best_translation)

        print(colorama.Style.RESET_ALL)

        return distance
