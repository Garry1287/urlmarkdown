import re
import os
import sys
import datetime
import pytz

# https://coderoad.ru/47204017/%D0%9E%D1%82%D0%BA%D1%80%D1%8B%D1%82%D0%B8%D0%B5-%D0%B8-%D1%87%D1%82%D0%B5%D0%BD%D0%B8%D0%B5-%D1%84%D0%B0%D0%B9%D0%BB%D0%BE%D0%B2-%D0%B2-%D0%BA%D0%B0%D1%82%D0%B0%D0%BB%D0%BE%D0%B3%D0%B5-%D0%B2-python-python-%D0%BD%D0%B0%D1%87%D0%B8%D0%BD%D0%B0%D1%8E%D1%89%D0%B8%D1%85
# https://coderoad.ru/40279488/%D0%9A%D0%B0%D0%BA-%D0%BF%D1%80%D0%BE%D1%87%D0%B8%D1%82%D0%B0%D1%82%D1%8C-%D0%BC%D0%BD%D0%BE%D0%B3%D0%BE-txt-%D1%84%D0%B0%D0%B9%D0%BB%D0%BE%D0%B2-%D0%B2-%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%BD%D0%BE%D0%B9-%D0%BF%D0%B0%D0%BF%D0%BA%D0%B5-%D1%81-%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E-python
# https://habr.com/ru/post/66931/ (по подошёл regex)
# https://medium.com/nuances-of-programming/%D1%88%D0%BF%D0%B0%D1%80%D0%B3%D0%B0%D0%BB%D0%BA%D0%B0-%D0%BF%D0%BE-%D1%80%D0%B5%D0%B3%D1%83%D0%BB%D1%8F%D1%80%D0%BD%D1%8B%D0%BC-%D0%B2%D1%8B%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F%D0%BC-%D0%B2-%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%D0%B0%D1%85-53820a5f3435
# https://pyneng.readthedocs.io/ru/latest/book/15_module_re/sub.html
# https://pythonru.com/primery/primery-primeneniya-regulyarnyh-vyrazheniy-v-python
# https://habr.com/ru/post/349860/#Primery_regulyarnyh_vyrazheniy
# https://regex101.com/
# https://pykili.github.io/prog/18-regexp-sub
# https://python-scripts.com/datetime-time-python
# https://yandex.ru/turbo/pythonist.ru/s/rabota-s-datoj-i-vremenem-modul-datetime/
# Наоборот
# https://habr.com/ru/post/190304/

path = sys.argv[1]
#path = "/home/garry/from-notebook/it-garry/MyBlog/iptech-blog/test/"
pattern = re.compile(r'(https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*))')


def create_file_header(FileName, MyDate):
    return """---
layout: post
title:  "%s"
date:   %s
categories: %s
---

# %s
""" % (FileName, MyDate.strftime("%Y-%m-%d %H:%M:%S %z"), FileName, FileName)


# returns the names of the files in the directory data as a list
list_of_files = os.listdir(path)
lines = []
for file in list_of_files:
    # Преобразование имени файла в markdown
    f = open(os.path.join(path + file), "r")
    MyDate = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
    # Формируем имя нового файла в виде дата-имя.markdown
    newfile = MyDate.strftime("%Y-%m-%d") + "-" + file.rpartition('.')[0] + ".markdown"
    fnew = open(os.path.join(path + newfile), "w")
    # Записываем в новый файл хедер
    fnew.write(create_file_header(file.rpartition('.')[0]), MyDate)
    # append each line in the file to a list
    lines = f.readlines()
    for line in lines:
        # print(line.strip())
        # print(pattern.sub(r'[\1](\1)', line))
        # В новый файл с расширение markdown записываем
        # преобразованные строки
        fnew.write(pattern.sub(r'[\1](\1)', line))
    f.close()
    fnew.close()
