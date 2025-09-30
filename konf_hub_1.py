import shlex
import os


class VFSEmulator:
    def __init__(self):
        self.vfs_name = "myvfs"
        self.current_dir = "/"
        self.running = True

    def print_prompt(self):
        print(f"{self.vfs_name}:{self.current_dir}$ ", end="")

    def parse_command(self, input_line):
        """Парсер команд с поддержкой кавычек"""
        try:
            return shlex.split(input_line)
        except ValueError as e:
            print(f"Ошибка парсинга: {e}")
            return []

    def cmd_ls(self, args):
        """Команда ls - заглушка"""
        print(f"ls: аргументы {args}")
        # Заглушка - в реальной реализации здесь был бы вывод файлов
        print("file1.txt  file2.txt  dir1/  dir2/")

    def cmd_cd(self, args):
        """Команда cd - заглушка"""
        print(f"cd: аргументы {args}")
        if args:
            new_dir = args[0]
            if new_dir == "..":
                # Упрощенная логика для перехода в родительскую директорию
                if self.current_dir != "/":
                    self.current_dir = os.path.dirname(self.current_dir.rstrip('/')) or "/"
            elif new_dir.startswith("/"):
                self.current_dir = new_dir
            else:
                self.current_dir = os.path.join(self.current_dir, new_dir)
            print(f"Переход в директорию: {self.current_dir}")
        else:
            print("Ошибка: cd требует аргумент")

    def cmd_exit(self, args):
        """Команда exit"""
        print("Выход из эмулятора")
        self.running = False

    def execute_command(self, command, args):
        """Выполнение команды"""
        commands = {
            "ls": self.cmd_ls,
            "cd": self.cmd_cd,
            "exit": self.cmd_exit
        }

        if command in commands:
            commands[command](args)
        else:
            print(f"Команда не найдена: {command}")

    def run(self):
        """Основной цикл REPL"""
        print("Эмулятор командной строки UNIX. Введите 'exit' для выхода.")

        while self.running:
            try:
                self.print_prompt()
                user_input = input().strip()

                if not user_input:
                    continue

                parts = self.parse_command(user_input)
                if not parts:
                    continue

                command = parts[0]
                args = parts[1:]

                self.execute_command(command, args)

            except KeyboardInterrupt:
                print("\nПрервано пользователем")
                break
            except EOFError:
                print("\nВыход")
                break
            except Exception as e:
                print(f"Неожиданная ошибка: {e}")


def main():
    emulator = VFSEmulator()
    emulator.run()
print("привет мир!")

if __name__ == "__main__":
    main()