#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import json
import xml
import os
import os.path as path
import chardet  # импортируем модуль для авто-определения кодировки текстового файла


def code_detecter(path_to_file_text):
    """
    Возвращает кодировку у данного тексторовго файла
    :param text:
    :return:
    """
    with open(path_to_file_text, 'rb') as source:  # бинарное чтение
        lines = source.read()
        result = chardet.detect(lines)
    if result['encoding'] is None:
        raise Exception("Неизвестная кодировка файла!")
    else:
        return result['encoding']


def tokenize(text):
    """
    Простейший токенизатор
    :param text:
    :return:
    """
    # Отставляем только буквы
    text_clear = ""
    for ch in text:
        if ch.isalpha() or ch == " ":
            text_clear += ch
    tokens = text_clear.split(" ")
    return tokens


def get_top(list_words, count_top):
    """
    Выводит первые count_top частотных слов
    :param list_words:
    :param count_top:
    :return:
    """
    list_words = sorted(list_words.items(), key=lambda item: item[1], reverse=True)
    return list_words[:count_top]

words = {}
max_length = 6
count_top = 10

# Загружаем новости из файлов в формате JSON
print("Загружаем слова из файлов (формат JSON), ждите ... ")
for file in os.listdir("."):
    try:
        if file.endswith(".json"):
            # print(code_detecter(file))
            with codecs.open(file, encoding=code_detecter(file)) as f:
                rss_news = json.load(f)
                for news in rss_news['rss']['channel']['item']:
                    if isinstance(news['description'], str):
                        input_text = news['description']
                    else:
                        input_text = news['description']['__cdata']
                    for new_word in tokenize(input_text):
                        if len(new_word) > max_length:
                            if words.get(new_word) is None:
                                words[new_word] = 0
                            else:
                                words[new_word] += 1
    except:
        print("Проблемма с обработкой файла с именем: %s" % file)

# Загружаем новости из файлов в формате XML
print("Загружаем слова из файлов (формат XML), ждите ... ")
for file in os.listdir("."):
    try:
        if file.endswith(".xml"):
            # print(code_detecter(file))
            with codecs.open(file, encoding=code_detecter(file)) as f:
                rss_news = json.load(f)
                for news in rss_news['rss']['channel']['item']:
                    if isinstance(news['description'], str):
                        input_text = news['description']
                    else:
                        input_text = news['description']['__cdata']
                    for new_word in tokenize(input_text):
                        if len(new_word) > max_length:
                            if words.get(new_word) is None:
                                words[new_word] = 0
                            else:
                                words[new_word] += 1
    except:
        print("Проблемма с обработкой файла с именем: %s" % file)



# Выводим TOP слов
print('Список из %d самых популярный слов:' % count_top)
for word, _ in get_top(words, count_top):
    print(word)