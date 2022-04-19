from colorama import init, Fore, Style


class ColorPrinter:
    @staticmethod
    def print_message_to_user(references: list[str], index: int, correction: list[bool], ratio: float) -> None:
        init()

        if ratio > 0.99:
            print(Fore.RED + "Correct.")

        elif ratio > 0.97:  # Во фразах очень много общего, показываем пользователю diff
            print(Fore.BLACK + "Almost correct. Right answer is: ", end='')
            ColorPrinter.print_colored_diff(correction, index, references)

        elif ratio > 0.65:  # Во фразах много общего, можно попробовать вывести пользователю diff
            print(Fore.BLACK + "Not bad. ", end='')
            print(Fore.BLACK + "Right answer is: ", end='')
            ColorPrinter.print_colored_diff(correction, index, references)
        else:
            print(Fore.RED + "Wrong. ", end='')  # Много ошибок, не пытаемся показать diff
            print(Fore.BLACK + "Right answer is: ", end='')
            print(Fore.GREEN + references[0])

        print(Style.RESET_ALL)

    @staticmethod
    def print_colored_diff(correction, index, references):
        for i, ch in enumerate(references[index]):
            if correction[i]:
                print(Fore.GREEN + ch, end='')
            else:
                if ch != " ":
                    print(Fore.RED + ch, end='')  # Just letter
                else:
                    if i - 1 >= 0 and i + 1 < len(references[index]):  # Подчеркиваем пробел среди верных, но слипшихся символов
                        if correction[i - 1] and correction[i + 1]:
                            print(Fore.RED + "_", end='')
                        else:
                            print(Fore.RED + " ", end='')
