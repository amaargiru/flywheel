from typing import List

from colorama import init, Fore, Style


class Printer:
    level4ratio: float = 0.99
    level3ratio: float = 0.97
    level2ratio: float = 0.65

    @staticmethod
    def color_print_message_to_user(references: List[str], index: int, correction: List[bool], ratio: float) -> None:
        init()

        if ratio > Printer.level4ratio:
            print(f"{Fore.GREEN}Correct.")
        elif ratio > Printer.level3ratio:  # Во фразах очень много общего, показываем пользователю diff
            print(f"{Fore.BLACK}Almost correct. Right answer is: ", end="")
            Printer.__print_colored_diff(correction, index, references)
        elif ratio > Printer.level2ratio:  # Во фразах много общего, можно попробовать вывести пользователю diff
            print(f"{Fore.BLACK}Not bad. ", end="")
            print(f"{Fore.BLACK}Right answer is: ", end="")
            Printer.__print_colored_diff(correction, index, references)
        else:
            print(f"{Fore.RED}Wrong. ", end="")
            print(f"{Fore.BLACK}Right answer is: ", end="")
            print(Fore.GREEN + references[0])

        print(Style.RESET_ALL)

    @staticmethod
    def __print_colored_diff(correction, index, references) -> None:
        for i, ch in enumerate(references[index]):
            if correction[i]:
                print(Fore.GREEN + ch, end="")
            elif ch == " ":
                if i >= 1 and i + 1 < len(references[index]):  # Подчеркиваем пробел среди верных, но слипшихся символов
                    if correction[i - 1] and correction[i + 1]:
                        print(f"{Fore.RED}_", end="")
                    else:
                        print(f"{Fore.RED} ", end="")

            else:
                print(Fore.RED + ch, end="")  # Just letter

    @staticmethod
    def format_message_to_api(references: List[str], index: int, correction: List[bool], ratio: float) -> dict:
        message_to_user = {"hint": Printer.__create_hint(correction, index, references)}

        if ratio > Printer.level4ratio:
            message_to_user["score"] = 4

        elif ratio > Printer.level3ratio:  # Во фразах очень много общего, показываем пользователю diff
            message_to_user["score"] = 3

        elif ratio > Printer.level2ratio:  # Во фразах много общего, можно попробовать вывести пользователю diff
            message_to_user["score"] = 2

        else:  # Много ошибок, не пытаемся показать diff
            message_to_user["score"] = 1

        return message_to_user

    @staticmethod
    def __create_hint(correction, index, references) -> str:
        hint_list: list = []

        for i, ch in enumerate(references[index]):
            if correction[i]:
                hint_list.append(ch)
            elif ch == " ":
                if i >= 1 and i + 1 < len(references[index]):  # Подчеркиваем пробел среди верных, но слипшихся символов
                    if correction[i - 1] and correction[i + 1]:
                        hint_list.append(f"/{ch}")
                    else:
                        hint_list.append(ch)

            else:
                hint_list.append(f"/{ch}")
        return "".join(hint_list)
