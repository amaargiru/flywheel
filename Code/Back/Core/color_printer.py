from colorama import init, Fore, Back, Style

class ColorPrinter:
    @staticmethod
    def color_print(references: list[str], index: int, correction: list[bool]) -> None:
        init()

        for i, ch in enumerate(references[index]):
            if correction[i]:
                print(Fore.GREEN + ch, end='')
            else:
                print(Fore.RED + ch, end='')

        print(Style.RESET_ALL)
