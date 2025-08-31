from sys import exit

class Security:
    # словарь с запрещёнными командами
    sett1 = {
        "sys.exit()",        # завершение программы
        "exit()",            # завершение программы
        "quit()",            # завершение программы
        "raise SystemExit",  # завершение программы
        "os.system",         # вызов системных команд
        "subprocess",        # выполнение внешних процессов
        "__import__",        # динамический импорт модулей
        "eval",              # выполнение произвольного кода
        "exec",              # выполнение произвольного кода
        "open",              # работа с файлами
        "del",               # удаление объектов
        "compile",           # компиляция кода
        "globals()",         # доступ к глобальной области
        "locals()",          # доступ к локальной области
        "vars()",            # доступ к переменным
        "__",                # любые двойные подчёркивания — часто системные атрибуты
    }

    @staticmethod
    def start_check(name_input):
        try:
            for i in name_input.split():
                if i in Security.sett1:
                    print("ты дурак? зачем ломать программу?")
                    exit()

        except (ZeroDivisionError, KeyboardInterrupt):
            print("ты дурак? зачем ломать программу?")