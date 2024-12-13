# 1. Подсчет слов в тексте


with open('text.txt', 'r', encoding='utf-8') as f:
  text = f.read()


word_count = len(text.split())


print(f"Количество слов в тексте: {word_count}")




# 2. Замена времени на TBD
import re

with open('letter.txt', 'r', encoding='utf-8') as f:
  text = f.read()


pattern = r'\d{2}:\d{2}:\d{2}|\d{2}:\d{2}' 
new_text = re.sub(pattern, '(TBD)', text)


print(f"Исправленный текст:\n{new_text}")
