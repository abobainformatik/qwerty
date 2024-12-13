import os
"""Задача 1"""
def read_last(lines, file):
    
    try:
        if not isinstance(lines, int) or lines <= 0:
            raise ValueError("lines должно быть положительным целым числом")

        with open(file, 'r', encoding='utf-8') as f:
            lines_list = f.readlines()
            if len(lines_list) < lines:
                print("В файле меньше строк, чем lines.")
                print("".join(lines_list)) 
            else:
                for line in lines_list[-lines:]:
                    print(line, end='')
    except FileNotFoundError:
        print(f"Файл {file} не найден.")
    except ValueError as e:
        print(f"Ошибка: {e}")

"""Задача 2"""
def print_docs(directory):
    
    try:
        for root, dirs, files in os.walk(directory):
            print(f"Директория: {root}")
            for file in files:
                print(f"  Файл: {file}")
    except FileNotFoundError:
        print(f"Директория {directory} не найдена.")

"""Задача 3"""
def longest_words(file):

    try:
        with open(file, 'r', encoding='utf-8') as f:
            text = f.read()
            words = text.split()
            max_len = 0
            longest_words_list = []

            for word in words:
                cleaned_word = ''.join(c for c in word if c.isalnum()) #убираем знаки препинания
                if len(cleaned_word) > max_len:
                    max_len = len(cleaned_word)
                    longest_words_list = [cleaned_word]
                elif len(cleaned_word) == max_len and len(cleaned_word)>0:
                    longest_words_list.append(cleaned_word)

            if len(longest_words_list)>0:
                print(f"Самое длинное слово (или слова): {longest_words_list}")
            else:
                print("Файл пуст или не содержит слов.")


    except FileNotFoundError:
        print(f"Файл {file} не найден.")

"""Задача 4"""
def simple_text_editor():
    """Простейший текстовый редактор."""
    filename = input("Введите имя файла (без расширения): ") + ".txt"
    with open(filename, 'w', encoding='utf-8') as f:
        while True:
            line = input("Введите строку (пустая строка для сохранения): ")
            if not line or line == ';' : #Спецсимвол ; для завершения
                break
            f.write(line + '\n')
    print(f"Файл {filename} сохранен.")
