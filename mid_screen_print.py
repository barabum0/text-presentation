# нужные вам настройки
text_to_find = "люблю всех, кто подписан на меня на гитхабе!!! ❤ ❤ ❤"
symbol_print_func = lambda sym: sym.replace("❤", ":heart:")

# symbol_print_func - функция, с которой будут выводиться печатаемые символы





# остальной код, который вас не интересует
import string
from random import choice
from time import sleep
from rich.console import Console
from rich.control import Control

letters = string.punctuation + string.ascii_letters + "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" + text_to_find
letters += letters.upper()

unique_letters = list(set(letters))

console = Console()

text_len = len(text_to_find)

start_x = ((console.size.width-text_len) // 2)-2
start_y = round(console.size.height / 2)-5

console.clear()
for index, symbol in enumerate(text_to_find):
    found: str = ""
    while symbol != found:
        found = choice(unique_letters)
        console.control(Control.move_to(x=start_x+index, y=start_y))
        console.print(f"[black on white]{symbol_print_func(found)}", end="")
        sleep(0.001)

    console.control(Control.move_to(x=start_x+index, y=start_y))
    console.print(f"{symbol_print_func(found)}", end="")

print("\n" * (console.size.height-start_y-3), end="")