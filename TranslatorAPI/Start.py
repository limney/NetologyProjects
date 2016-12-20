#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Translator import Translator
import os

KEY = 'trnsl.1.1.20161216T160124Z.4a07c4b6a2f01566.ade260e6c684818698899fd08a9c15d72faca843'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

translator = Translator(KEY, URL)  # создали экземпляр класса Переводчик

folder_source = os.path.normpath(os.path.join(os.path.dirname(__file__), "Files_texts"))  # папка с текстовыми файлами
folder_output = os.path.normpath(os.path.join(os.path.dirname(__file__), "Output_files"))  # папка с текстовыми файлами

count_translated_files = 0  # количество успешно переведенных файлов

# Перебираем файлы из папки
for cur_file in os.listdir(folder_source):
    code_lang, _ = os.path.splitext(cur_file)  # имя файла указывает на код языка текста в нем
    translator.lang = code_lang, "ru"  # направление перевода
    source_file = os.path.join(folder_source, cur_file)  # source_file
    output_file = os.path.join(folder_output, cur_file)  # output file
    with open(output_file, 'w', encoding="UTF-8") as write_f:
        with open(source_file, 'r', encoding="UTF-8") as read_f:
            translated_text = translator.translate_me(read_f.readlines())
            write_f.writelines(translated_text["text"])
            count_translated_files += 1

print("Готово!\nПеревели: %d файлов" % count_translated_files)





