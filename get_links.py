import re
"""
Модуль читает файл и находит в нём информацию с помощью регулярных выражений.

"""

wiki_text_file = 'python_wiki.txt'
links_text_file = 'links.txt'
d_brakets = r'\[{2}'
d_brakets2 = r'\]{2}'
code = r'\[{2}([^\|\]]*)(\|{1}|\]{2})'
regexp_d_brakets = re.compile(d_brakets)
regexp_d_brakets2 = re.compile(d_brakets2)
regexp = re.compile(code)

with open(wiki_text_file, 'r', encoding='utf-8') as f:
    text = f.read()
    matches_d_brakets = regexp_d_brakets.findall(text)
    matches_d_brakets2 = regexp_d_brakets2.findall(text)
    matches = regexp.findall(text)

links = list(sorted(set(l[0] for l in matches)))

with open(links_text_file, 'w', encoding='utf-8') as f:
    for line in links:
        f.write(line + '\n')

with open(links_text_file, 'r', encoding='utf-8') as f:
    lines = len([lines for lines in f])

# Подготовка данных для вывода
attributes = (
'Обработка файла:',
'Количество совпадений по шаблону "' + d_brakets + '":',
'Количество совпадений по шаблону "' + d_brakets2 + '":',
'Количество совпадений по шаблону "' + code + '":',
'Количество уникальных ссылок:',
'Запись ссылок в файл:',
'Количество строк в файле:',
)

values = (
wiki_text_file,
len(matches_d_brakets),
len(matches_d_brakets2),
len(matches),
len(links),
links_text_file,
lines
)

fill = '<'
align = max([len(str_lengt) for str_lengt in attributes])

# Захотел применить функцию zip и 
# сократить кол-во строк print для удобства изменения форматирования вывода
for attribute, value in zip(attributes, values):
    print('{:{fill}{align}} {}'.format(attribute, value, fill=fill, align=align))


# print('{:{fill}{align}} {}'.format('Обработка файла:', wiki_text_file, fill=fill, align=align))
# print('{:{fill}{align}} {}'.format('Количество совпадений по шаблону "'+d_brakets+'":', len(matches_d_brakets), fill=fill, align=align))
# print('{:{fill}{align}} {}'.format('Количество совпадений по шаблону "'+code+'":', len(matches), fill=fill, align=align))
# print('{:{fill}{align}} {}'.format('Количество уникальных ссылок:', len(links), fill=fill, align=align))
# print('')
# print('{:{fill}{align}} {}'.format('Запись ссылок в файл:', links_text_file, fill=fill, align=align))
# print('{:{fill}{align}} {}'.format('Количество строк в файле:', lines, fill=fill, align=align))
