# Завдання 1

def total_salary(path):
    try:
        total = 0
        count = 0
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary = line.strip().split(',')
                total += int(salary)
                count += 1

        average = total / count if count > 0 else 0
        return total, average
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        return 0, 0

# Завдання 2

def get_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cat_info = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }
                cats_list.append(cat_info)
        return cats_list
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return []
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        return []

# Завдання 3

import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

def print_directory_structure(path, indent_level=0):
    try:
        directory = Path(path)

        if not directory.exists():
            print(Fore.RED + f"Помилка: Шлях '{path}' не існує.")
            return

        if not directory.is_dir():
            print(Fore.RED + f"Помилка: Шлях '{path}' не є директорією.")
            return

        for item in sorted(directory.iterdir(), key=lambda x: (x.is_file(), x.name.lower())):
            if item.is_dir():
                print(" " * indent_level + Fore.BLUE + f"📂 {item.name}")
                print_directory_structure(item, indent_level + 4)
            else:
                print(" " * indent_level + Fore.GREEN + f"📜 {item.name}")
    except Exception as e:
        print(Fore.RED + f"Сталася помилка: {e}")

def main():
    if len(sys.argv) != 2:
        print(Fore.RED + "Будь ласка, надайте шлях до директорії як аргумент командного рядка.")
        print(Fore.YELLOW + "Приклад: python hw03.py /шлях/до/директорії")
        return

    directory_path = sys.argv[1]
    print_directory_structure(directory_path)

if __name__ == "__main__":
    main()
