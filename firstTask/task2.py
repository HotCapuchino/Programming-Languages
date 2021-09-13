import re

word = input('Введите слово на английском: ')
regex_wovels = r'[aeiou]'
regex_consonant = r'[bcdfghjklmnpqrstvwxyz]'
result_wovels = re.findall(regex_wovels, word, re.IGNORECASE)
result_consonants = re.findall(regex_consonant, word, re.IGNORECASE)

print(f'Количество гласных: {len(result_wovels)}')
print(f'Количество согласных: {len(result_consonants)}')
