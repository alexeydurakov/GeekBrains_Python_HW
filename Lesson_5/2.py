# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('text_for_2.txt', 'r', encoding='utf-8') as f:
    text_line = f.readlines()
print(text_line)
for el in text_line:
    print(len(el.split()))

print([len(el.split()) for el in text_line])