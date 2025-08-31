from security import Security
import logging
from sys import exit

logging.basicConfig(level=logging.DEBUG) # делаем чтобы DEBUG и INFO не игнорировались

try:
    path = input("введите путь до файла с кодом: ")
    Security.start_check(path) #проверяем input на наличие небезопасных команд

    with open(fr"{path}", "r", encoding="utf-8") as f:
        read_code = f.read()
    
    #делаем код нечитаемым
    new_code = f"""

    {read_code}

    """.strip().split()
except (FileNotFoundError, NameError):
    logging.error("ошибка: такого файла не существует.")
    exit()

choice = input("код успешно переделан, показать сейчас? (да/нет): ").lower()
Security.start_check(path)

if choice == "да":
    print(f"код:\n{new_code}")  
else:
    print("ну ладно")
