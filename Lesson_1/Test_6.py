# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
#  Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.

import locale

test_string = ['сетевое программирование', 'сокет', 'декоратор']

#Создаем файл
with open('test_file.txt', 'w+') as f:
    for i in test_string:
        f.write(i + '\n')
    f.seek(0)

# печатаем объект файла, что бы узнать его кодировку
print(f)

file_coding = locale.getpreferredencoding()

# Читаем из файла
with open('test_file.txt', 'r', encoding=file_coding) as f:
    for i in f:
        print(i)

    f.seek(0)
