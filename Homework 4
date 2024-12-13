# Задача 1: Подсчет и замена последовательности "н"

def longest_n_sequence(text):

  max_n_count = 0
  current_n_count = 0
  longest_n_index = -1

  for i, char in enumerate(text):
    if char == 'n':
      current_n_count += 1
    else:
      if current_n_count > max_n_count:
        max_n_count = current_n_count
        longest_n_index = i - current_n_count
      current_n_count = 0

  if current_n_count > max_n_count: 
    max_n_count = current_n_count
    longest_n_index = len(text) - current_n_count

  if max_n_count > 0:
    new_text = list(text)
    new_text[longest_n_index:longest_n_index + max_n_count] = ['!'] * max_n_count
    new_text = "".join(new_text)
  else:
    new_text = text

  return new_text, max_n_count


text = "nnnnnnnnyufnnnnnnn"
new_text, count = longest_n_sequence(text)
print(f"Новая строка: {new_text}")
print(f"Количество подряд идущих 'n': {count}")



# Задача 2: Вывод символов внутри скобок

def chars_inside_brackets(text):

  open_bracket_index = text.find('(')
  if open_bracket_index == -1:
    return ""

  close_bracket_index = text.find(')', open_bracket_index)
  if close_bracket_index == -1:
    return ""

  return text[open_bracket_index + 1:close_bracket_index]


text = "hjhbkhwbk(kkjbkj)"
result = chars_inside_brackets(text)
print(f"Символы внутри скобок: {result}")


# Задача 3: Вывод слов, начинающихся на "а" и заканчивающихся на "я"

import re

def words_starting_a_ending_ya(text):

  words = re.findall(r'\b[аА][а-яА-Я]*я\b', text) # \b - граница слова
  return words

text = "Абстракция авария аллея Абракадабра Банальная история"
result = words_starting_a_ending_ya(text)
print(f"Слова, начинающиеся на 'а' и заканчивающиеся на я {result}")
