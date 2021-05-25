import re
import os
import sys
import datetime
import pytz
from random import randrange
from datetime import timedelta

# #python3 urlmarkdown-randomdate.py /home/garry/from-notebook/it-garry/MyBlog/iptech-blog/test/
# Для старых файлов рандомно выставляем время

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def create_file_header(FileName, MyRandomDate, MyDir):
    return """---
layout: post
title:  "%s"
date:   %s
categories: %s
tags: %s
---

# %s
""" % (FileName, MyRandomDate.strftime("%Y-%m-%d %H:%M:%S %z"), FileName, MyDir, FileName)


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

# Пришёл в PSI
d1 = datetime.datetime.strptime("1.12.2008 00:00", "%d.%m.%Y %H:%M")
# Делал эти заметки до этого времени
d2 = datetime.datetime.strptime('31.12.2018 23:59', "%d.%m.%Y %H:%M")

tz_moscow = pytz.timezone('Europe/Moscow')



#(random_date(d1, d2))






# returns the names of the files in the directory data as a list
list_of_files = os.listdir(path)
lines = []
for file in list_of_files:
    # Преобразование имени файла в markdown
    f = open(os.path.join(path + file), "r")
    MyRandomDate = tz_moscow.localize(random_date(d1, d2))
    newfile = MyRandomDate.strftime("%Y-%m-%d") + "-" + file.rpartition('.')[0] + ".markdown"
    fnew = open(os.path.join(path + newfile), "w")
    fnew.write(create_file_header(file.rpartition('.')[0], MyRandomDate, path.split("/")[-2]))
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
