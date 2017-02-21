#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from ClientVK import *
import os
import time
import threading

MY_APP_ID = 5786550
TOP = 5  # выбираем первые 5 групп из списка top100



if __name__ == "__main__":

    vk = ClientVK(app_id=MY_APP_ID)

    top5 = []
    # Загружаем TOP 100 групп подписчиков у пользователя (Гарика Харламова)
    with open('top100.json', 'r', encoding="UTF-8") as file:
        groups_raw = json.load(file)
        for group in groups_raw[:TOP]:
            top5.append(group)

    # Сбор людей в каждой из групп
    for group in top5:
        groups_members = vk.get_members(group["id"])
        group["members"] = groups_members

    # Запись в файл
    with open('top5.txt', 'a', encoding="UTF-8") as file:
        file.write("id_group\ttitle\tuid_user\tsex\tage")
        for group in top5:
            for member in group["members"]:
                line = str(group["id"]) + "\t" + group["title"] + "\t" + str(member["uid"]) + "\t" + member["sex"] + "\t" + str(member["age"]) + "\n"
                file.write(line)

